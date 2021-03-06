# ===========================================================================
# Author:       Max ZIMMER
# Project:      NashFlowComputation 2017
# File:         plotCanvasClass.py
# Description:  Class to plot networkx graphs in widgets and control click events
# ===========================================================================

from math import sqrt

import matplotlib.figure
import networkx as nx
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.colors import colorConverter
from networkx import draw_networkx_labels, draw_networkx_edge_labels

from source.utilitiesClass import Utilities

# Config
SIMILARITY_DIST = 9  # Maximal distance at which a click is recognized as a click on a node/edge


# ======================================================================================================================


class PlotCanvas(FigureCanvas):
    """Class to plot networkx graphs in widgets and control click events"""

    def __init__(self, graph, interface, stretchFactor=1.57, onlyNTF=False, type='general', showArrows=True):
        self.figure = matplotlib.figure.Figure()
        super(PlotCanvas, self).__init__(self.figure)  # Call parents constructor
        self.figure.patch.set_facecolor('lightgrey')
        self.network = graph
        self.interface = interface
        self.onlyNTF = onlyNTF  # If this is true, then PlotCanvas belongs to Thinflow Computation App
        self.type = type  # 'general' or 'spillback'
        self.showArrows = showArrows

        # Visualization Settings
        sqSize = 120
        self.Xlim = (stretchFactor * (-sqSize), stretchFactor * sqSize)
        self.Ylim = (-sqSize, sqSize)
        self.nodeSize = 24 ** 2
        self.nodeLabelFontSize = 9  # float but passed as int
        self.edgeLabelFontSize = 7  # float but passed as int
        self.edgeWidthSize = 4

        # Only one of them can be not None
        self.focusNode = None
        self.focusEdge = None

        # Internal variables
        self.selectedNode = None

        # Signals
        self.mpl_connect('button_press_event', self.on_click)
        self.mpl_connect('button_release_event', self.on_release)
        self.mpl_connect('motion_notify_event', self.on_motion)
        self.mpl_connect('scroll_event', self.on_scroll)

        # Mouse events
        # Mouse wheel
        self.mouseWheelPressedPosition = None
        self.mouseWheelPressed = False

        # Mouse right
        self.mouseRightPressed = False

        self.init_plot()  # Plot for the first time

    def get_additional_node_labels(self):
        """Returns dict of additional node labels"""
        return {}

    def get_edge_labels(self):
        """Returns dict of edge labels"""
        if self.type == 'general':
            attributes = ['outCapacity', 'transitTime'] if not self.onlyNTF else ['outCapacity']
            multipleBool = (len(attributes) > 1)
        elif self.type == 'spillback':
            attributes = ['inCapacity', 'outCapacity', 'storage', 'transitTime'] if not self.onlyNTF \
                            else ['outCapacity'] # 'inflowBound' has to be added manually below
            multipleBool = True
        attributeList = [nx.get_edge_attributes(self.network, attr) for attr in attributes]
        if (self.type == 'spillback' and self.onlyNTF):
            attr = 'inflowBound'
            d = dict()
            for e in self.network.edges():
                (v, w) = e
                d[e] = self.network[v][w]['TFC'][attr]
            attributeList.append(d)

        labelDict = Utilities.join_intersect_dicts(*attributeList)

        # Integer values should be displayed in shortest possible way
        for key, valTuple in labelDict.items():
            if not multipleBool:
                if valTuple != float('inf') and valTuple == int(valTuple):
                    labelDict[key] = int(valTuple)
            else:
                newTuple = []
                for val in valTuple:
                    newTuple.append(int(val) if (val != float('inf') and int(val) == val) else val)
                labelDict[key] = tuple(newTuple)
        return labelDict

    def on_click(self, event):
        """
        Onclick-event handling
        :param event: event which is emitted by matplotlib
        """

        if event.xdata is None or event.ydata is None:
            return

        # Note: event.x/y = relative position, event.xdata/ydata = absolute position
        xAbsolute, yAbsolute = event.xdata, event.ydata

        action = event.button  # event.button = mouse(1,2,3)

        if action == 1:
            # Leftmouse was clicked, select/create node, select edge or add edge via drag&drop

            lastID = self.network.graph['lastID']

            # Determine whether we clicked an edge or not
            clickedEdge = self.check_edge_clicked((xAbsolute, yAbsolute))

            # Determine whether we clicked a node or not
            clickedNode = self.check_node_clicked((xAbsolute, yAbsolute), edgePossible=(clickedEdge is not None))
            newNodeCreated = (self.network.graph['lastID'] > lastID)

            if clickedEdge is not None and clickedNode is None:
                # Selected an existing edge
                self.focusEdge = clickedEdge
                self.focusNode = None

                self.interface.update_node_display()
                self.interface.update_edge_display()
                self.update_nodes(color=True)
                self.update_edges(color=True)
            elif clickedNode is not None:
                self.focusNode = clickedNode
                self.focusEdge = None
                self.update_edges(color=True)
                self.interface.update_edge_display()
                self.selectedNode = clickedNode
                self.update_nodes(added=newNodeCreated, color=True)

                if newNodeCreated:
                    self.interface.add_node_to_list(self.focusNode)

        elif action == 2:
            # Wheel was clicked, move visible part of canvas
            self.mouseWheelPressed = True
            self.mouseWheelPressedPosition = (xAbsolute, yAbsolute)
            return

        elif action == 3:
            clickedNode = self.check_node_clicked((xAbsolute, yAbsolute), edgePossible=True)
            if clickedNode is not None:
                self.selectedNode = clickedNode
                self.mouseRightPressed = True
                self.focusNode = self.selectedNode
                self.focusEdge = None
                self.update_edges(color=True)
                self.update_nodes(color=True)
                self.interface.update_edge_display()
                self.interface.update_node_display()

    def on_release(self, event):
        """
        Release-Mouse-event handling
        :param event: event which is emitted by matplotlib
        """
        if event.xdata is None or event.ydata is None:
            return
        xAbsolute, yAbsolute = event.xdata, event.ydata
        action = event.button  # event.button = mouse(1,2,3)

        if action == 1:
            # Leftmouse has been released
            # Determine whether we clicked a node or not (or create one!)
            lastID = self.network.graph['lastID']
            clickedEdge = self.check_edge_clicked((xAbsolute, yAbsolute))
            clickedNode = self.check_node_clicked((xAbsolute, yAbsolute), edgePossible=(clickedEdge is not None))
            newNodeCreated = (self.network.graph['lastID'] > lastID)
            if clickedNode is not None:
                if newNodeCreated:
                    self.focusNode = clickedNode
                    self.update_nodes(added=True, color=True)
                    self.interface.add_node_to_list(clickedNode)
                    self.focusNode = None

                if self.selectedNode is not None and self.selectedNode != clickedNode:
                    # Add the corresponding edge, if valid
                    if not self.network.has_edge(self.selectedNode, clickedNode):
                        resettingEnabledBool = False if self.onlyNTF else None  # Either 0 or 1. Activated only if onlyNTF
                        activeEnabledBool = True if self.onlyNTF else None  # Either 0 or 1. Activated only if onlyNTF
                        if self.type == 'general':
                            self.network.add_edge(self.selectedNode, clickedNode, transitTime=1,
                                                  inCapacity=float('inf'), outCapacity=1, storage=float('inf'),
                                                  TFC={'resettingEnabled':resettingEnabledBool,
                                                       'active':activeEnabledBool})
                        elif self.type == 'spillback':
                            self.network.add_edge(self.selectedNode, clickedNode, transitTime=1,
                                                  inCapacity=float('inf'), outCapacity=1, storage=float('inf'),
                                                  TFC={'resettingEnabled':resettingEnabledBool, 'inflowBound':1,
                                                       'active':activeEnabledBool})

                        self.focusEdge = (self.selectedNode, clickedNode)
                        self.focusNode = None

                        self.interface.update_edge_display()
                        self.update_edges(added=True, color=True)
                        self.interface.add_edge_to_list(self.focusEdge)

            self.selectedNode = None
            self.update_nodes(color=True)

            self.interface.update_node_display()

        elif action == 2:
            # Wheel has been released
            self.mouseWheelPressed = False
            self.mouseWheelPressedPosition = None

        elif action == 3:
            # Right mouse has been released
            self.mouseRightPressed = False
            self.selectedNode = None

    def on_motion(self, event):
        """
        Move-Mouse-event handling
        :param event: event which is emitted by matplotlib
        """
        if event.xdata is None or event.ydata is None:
            return

        # Note: event.x/y = relative position, event.xdata/ydata = absolute position
        xAbsolute, yAbsolute = event.xdata, event.ydata

        if self.mouseWheelPressed and self.mouseWheelPressedPosition is not None:
            self.mouseWheelPosition = (xAbsolute, yAbsolute)
            self.move()
            self.draw_idle()

        elif self.mouseRightPressed and self.selectedNode is not None:
            self.network.nodes[self.selectedNode]['position'] = (xAbsolute, yAbsolute)
            self.update_nodes(moved=True, color=True)
            self.update_edges(moved=True)
            self.interface.update_node_display()

    def on_scroll(self, event):
        """
        Scroll-Mouse-event handling
        :param event: event which is emitted by matplotlib
        """
        if event.xdata is None or event.ydata is None:
            return

        action = event.button  # 'up'/'down' Note: 'up' == zoom in,'down' == zoom out
        sFactor = 1 - 0.1  # zoom out velocity
        bFactor = 1. / sFactor  # zoom in velocity, chosen s.t. sFactor * bFactor ~=ye 1

        factor = bFactor if action == 'up' else sFactor
        self.zoom(factor)

    def check_edge_clicked(self, clickpos):
        """
        Check whether a given click position clickpos was a click on an edge
        :param clickpos: tuple containing absolute x and y value of click event
        :return: clicked edge (None if no edge has been selected)
        """
        clickedEdge = None
        for edge in self.network.edges():
            startpos = self.network.nodes[edge[0]]['position']
            endpos = self.network.nodes[edge[1]]['position']
            dist = self.compute_dist_projection_on_segment(clickpos, startpos, endpos)
            if 0 <= dist <= SIMILARITY_DIST:
                clickedEdge = edge
                break
        return clickedEdge

    @staticmethod
    def compute_dist_projection_on_segment(clickpos, startpos, endpos):
        """
        Compute distance between clickpos and its  vertical projection on line segment [startpos, endpos]
        :param clickpos: tuple containing absolute x and y value of click event
        :param startpos: tuple specifying start of line segment
        :param endpos: tuple specifying end of line segment
        :return: distance (-1 if projection does not lie on segment)
        """
        # Subtract startpos to be able to work with vectors
        mu = np.array(clickpos) - np.array(startpos)
        b = np.array(endpos) - np.array(startpos)

        xScalar = (np.dot(mu, b) / (np.linalg.norm(b)) ** 2)
        x = xScalar * b

        if xScalar < 0 or xScalar > 1:
            # The perpendicular projection of mu onto b does not lie on the segment [0, b]
            return -1
        else:
            # Return distance of projection to vector itself
            return np.linalg.norm(mu - x)

    def check_node_clicked(self, clickpos, edgePossible=False):
        """
        Check whether a given click position clickpos was a click on a node
        Creates a node if clickpos is not too close to existing nodes
        :param clickpos: tuple containing absolute x and y value of click event
        :param edgePossible: bool indicating whether click corresponds to an edge
        :return: clicked node (None if no node has been selected)
        """

        xAbsolute, yAbsolute = clickpos[0], clickpos[1]
        clickedNode = None
        minDist = float('inf')
        positions = nx.get_node_attributes(self.network, 'position')
        for node, pos in positions.items():
            dist = sqrt((xAbsolute - pos[0]) ** 2 + (yAbsolute - pos[1]) ** 2)
            if dist <= SIMILARITY_DIST:
                clickedNode = node
                break
            elif dist <= minDist:
                minDist = dist

        if clickedNode is None and minDist > 2 * SIMILARITY_DIST and not edgePossible:
            # Create new node
            nodeID = str(self.network.graph['lastID'])
            self.network.add_node(nodeID)
            self.network.nodes[nodeID]['position'] = (int(xAbsolute), int(yAbsolute))
            self.network.nodes[nodeID]['label'] = nodeID
            self.network.graph['lastID'] += 1
            return nodeID
        return clickedNode

    def edgeColor(self, v, w):
        """
        Function returning the color that should be used while drawing edges
        :param v: tail node
        :param w: head node
        :return: Color string (e.g. 'b', 'black', 'red' et cetera)
        """
        if (v, w) == self.focusEdge:
            return "b"  # Blue
        elif self.onlyNTF:
            # Color resetting edges (those that have been selected by the user to be as such) differently
            if not self.network[v][w]['TFC']['active']:
                return 'gray'
            if self.network[v][w]['TFC']['resettingEnabled']:
                return 'r'  # Red
        return 'black'  # Don't color resetting edges, thus edge should be black

    def init_plot(self):
        """
        Update canvas to plot new graph
        """
        self.figure.clf()  # Clear current figure window
        self.axes = self.figure.add_axes([0, 0, 1, 1])
        # self.axes.set_aspect("equal")
        self.axes.set_xlim(self.Xlim)
        self.axes.set_ylim(self.Ylim)

        self.axes.axis('off')  # Hide axes in the plot

        nodeLabelSize = int(round(self.nodeLabelFontSize))
        edgeLabelSize = int(round(self.edgeLabelFontSize))

        positions = nx.get_node_attributes(self.network, 'position')

        # Plot Nodes
        self.nodeCollections = []
        nodeColor = lambda v: 'r' if v != self.focusNode else 'b'
        nodeColorList = [nodeColor(v) for v in self.network.nodes()]
        self.nodeCollections.append((list(self.network.nodes()),
                                     self.draw_nodes(self.network, pos=positions, ax=self.axes,
                                                     node_size=self.nodeSize, node_color=nodeColorList)))

        # Plot Node Labels
        self.nodeLabelCollection = draw_networkx_labels(self.network, pos=positions, ax=self.axes,
                                                        labels=nx.get_node_attributes(self.network, 'label'),
                                                        font_size=nodeLabelSize)

        # Plot Edges
        self.edgeCollections, self.boxCollections, self.arrowCollections = [], [], []
        edgeColorList = [self.edgeColor(v, w) for v, w in self.network.edges()]
        if edgeColorList:
            edgeCollection, boxCollection, arrowCollection = self.draw_edges(self.network, pos=positions, ax=self.axes,
                                                            arrow=True,
                                                            edge_color=edgeColorList, width=self.edgeWidthSize)
            self.edgeCollections.append((list(self.network.edges()), edgeCollection))
            self.boxCollections.append((list(self.network.edges()), boxCollection))
            self.arrowCollections.append((list(self.network.edges()), arrowCollection))

        additionalNodeLabels = self.get_additional_node_labels()
        if additionalNodeLabels:
            # Plot Nash Flow Node Labels
            offset = (0, 15)
            add_tuple_offset = lambda a: (a[0] + offset[0], a[1] + offset[1])
            movedPositions = {node: add_tuple_offset(positions[node]) for node in positions}
            self.additionalNodeLabelCollection = draw_networkx_labels(self.network, pos=movedPositions, ax=self.axes,
                                                                      labels=additionalNodeLabels,
                                                                      font_size=nodeLabelSize)
        else:
            self.additionalNodeLabelCollection = {}

        self.edgeLabels = self.get_edge_labels()

        self.edgeLabelCollection = draw_networkx_edge_labels(self.network, pos=positions, ax=self.axes,
                                                             edge_labels=self.edgeLabels, font_size=edgeLabelSize)

        self.draw_idle()

    def update_plot(self):
        """Update the entire plot"""
        self.update_nodes()
        self.update_edges()

    def update_nodes(self, added=False, removal=False, moved=False, color=False):
        """
        Redraw node(s)
        :param added: If True then a node has been added
        :param removal: If True then a node has been removed
        :param moved: If True then a node has been moved
        :param color: If True then the color of a node has changed
        """
        nodeLabelSize = int(round(self.nodeLabelFontSize))
        if removal or moved:
            # A node has been deleted
            v = self.focusNode
            collectionIndex = 0
            for nodes, nodeCollection in self.nodeCollections:
                if v in nodes:
                    nodeCollection.remove()
                    nodes = [node for node in nodes if node != v]
                    if nodes:
                        positions = {v: self.network.nodes[v]['position'] for v in self.network.nodes()}
                        newNodeCollection = self.draw_nodes(self.network,
                                                            pos=positions,
                                                            ax=self.axes, node_size=self.nodeSize,
                                                            nodelist=nodes, node_color='r')
                        self.nodeCollections[collectionIndex] = (nodes, newNodeCollection)
                    else:
                        del self.nodeCollections[collectionIndex]

                    break

                collectionIndex += 1
            if not moved:
                # Delete node label
                deletedLabel = self.nodeLabelCollection.pop(self.focusNode)
                deletedLabel.remove()

            else:
                self.nodeCollections.append(([v], self.draw_nodes(self.network,
                                                                  pos={v: self.network.nodes[v]['position']},
                                                                  ax=self.axes, node_size=self.nodeSize,
                                                                  nodelist=[v], node_color='b')))
        elif added:
            # A node has been added (can we do better than plotting all nodes again?)
            if self.focusNode is not None and all([self.focusNode not in entry for entry in self.nodeCollections]):
                v = self.focusNode
                self.nodeCollections.append(([v], self.draw_nodes(self.network,
                                                                  pos={v: self.network.nodes[v]['position']},
                                                                  ax=self.axes, node_size=self.nodeSize,
                                                                  nodelist=[v])))
                self.nodeLabelCollection.update(
                    draw_networkx_labels(self.network, pos={v: self.network.nodes[v]['position']}, ax=self.axes,
                                         labels={v: self.network.nodes[v]['label']}, font_size=nodeLabelSize))

        # Update node label texts and positions
        for v, label in self.nodeLabelCollection.items():  # type(label) = matplotlib.text.Text object
            if label.get_text() != self.network.nodes[v]['label']:
                label.remove()
                self.nodeLabelCollection[v] = \
                    draw_networkx_labels(self.network, pos={v: self.network.nodes[v]['position']}, ax=self.axes,
                                         labels={v: self.network.nodes[v]['label']}, font_size=nodeLabelSize)[v]
            elif v == self.focusNode and moved:
                label.set_position(self.network.nodes[v]['position'])

        if color:
            nodeColor = lambda v: 'r' if v != self.focusNode else 'b'
            # Update colors and position
            for nodes, nodeCollection in self.nodeCollections:
                nodeColorList = [nodeColor(v) for v in nodes] if not removal else 'r'
                nodeCollection.set_facecolors(nodeColorList)

        self.draw_idle()

    def update_edges(self, added=False, removal=False, moved=False, color=False):
        """
        Redraw edges(s)
        :param added: If True then an edge has been added
        :param removal: If True then an edge has been removed
        :param moved: If True then an edge has been moved
        :param color: If True then the color of an edge has changed
        """
        if removal:
            # Edges have been deleted
            collectionIndex = 0
            toDeleteIndices = []
            for edges, edgeCollection in self.edgeCollections:
                missingEdges = [edge for edge in edges if edge not in self.network.edges()]
                if missingEdges:
                    boxCollection = self.boxCollections[collectionIndex][1]
                    arrowCollection = self.arrowCollections[collectionIndex][1]
                    edgeCollection.remove()
                    boxCollection.remove()
                    arrowCollection.remove()

                    edges = [edge for edge in edges if edge not in missingEdges]
                    if edges:
                        positions = {v: self.network.nodes[v]['position'] for v in self.network.nodes()}
                        newEdgeCollection, newBoxCollection, newArrowCollection = self.draw_edges(self.network, pos=positions,
                                                                              ax=self.axes, arrow=True,
                                                                              edgelist=edges, width=self.edgeWidthSize)
                        self.edgeCollections[collectionIndex] = (edges, newEdgeCollection)
                        self.boxCollections[collectionIndex] = (edges, newBoxCollection)
                        self.arrowCollections[collectionIndex] = (edges, newArrowCollection)

                    else:
                        toDeleteIndices.append(collectionIndex)

                    # Delete edge labels
                    for edge in missingEdges:
                        deletedLabel = self.edgeLabelCollection.pop(edge)
                        deletedLabel.remove()

                collectionIndex += 1

            for index in reversed(toDeleteIndices):
                del self.edgeCollections[index]
                del self.boxCollections[index]
                del self.arrowCollections[index]


        elif added:
            # A node has been added (can we do better than plotting all nodes again)
            if self.focusEdge is not None:
                v, w = self.focusEdge
                edgeCollection, boxCollection, arrowCollection = self.draw_edges(self.network,
                                                                pos={v: self.network.nodes[v]['position'],
                                                                     w: self.network.nodes[w]['position']},
                                                                ax=self.axes, arrow=True,
                                                                edgelist=[self.focusEdge],
                                                                width=self.edgeWidthSize)

                self.edgeCollections.append(([self.focusEdge], edgeCollection))
                self.boxCollections.append(([self.focusEdge], boxCollection))
                self.arrowCollections.append(([self.focusEdge], arrowCollection))
                edgeLabelSize = int(round(self.edgeLabelFontSize))
                if not self.onlyNTF:
                    if self.type == 'general':
                        lbl = {self.focusEdge: (self.network[v][w]['outCapacity'], self.network[v][w]['transitTime'])}
                    elif self.type == 'spillback':
                        lbl = {self.focusEdge: (self.network[v][w]['inCapacity'], self.network[v][w]['outCapacity'],
                                                self.network[v][w]['transitTime'], self.network[v][w]['storage'])}
                else:
                    if self.type == 'general':
                        lbl = {self.focusEdge: (self.network[v][w]['outCapacity'])}
                    elif self.type == 'spillback':
                        lbl = {self.focusEdge: (self.network[v][w]['outCapacity'], self.network[v][w]['TFC']['inflowBound'])}
                self.edgeLabelCollection.update(draw_networkx_edge_labels(self.network,
                                                                          pos={v: self.network.nodes[v]['position'],
                                                                               w: self.network.nodes[w]['position']},
                                                                          ax=self.axes, edge_labels=lbl,
                                                                          font_size=edgeLabelSize))

        elif moved:
            collectionIndex = 0
            for edges, edgeCollection in self.edgeCollections:
                pos = nx.get_node_attributes(self.network, 'position')

                p = 0.3
                edge_pos = []
                for edge in edges:
                    src, dst = np.array(pos[edge[0]]), np.array(pos[edge[1]])
                    s = dst - src
                    # src = src + p * s  # Box at beginning
                    # dst = src + (1 - p) * s  # Box at the end
                    dst = src  # No edge at all
                    edge_pos.append((src, dst))

                edge_pos = np.asarray(edge_pos)
                box_pos = np.asarray([(pos[e[0]], pos[e[1]]) for e in edges])
                # Move edges
                edgeCollection.set_segments(edge_pos)

                boxCollection = self.boxCollections[collectionIndex][1]
                # Move boxes
                boxCollection.remove()
                boxCollection = Utilities.get_boxes(edge_pos=box_pos)
                boxCollection.set_zorder(1)  # edges go behind nodes
                # boxCollection.set_label(label)
                self.axes.add_collection(boxCollection)
                self.boxCollections[collectionIndex] = (self.boxCollections[collectionIndex][0], boxCollection)

                arrowCollection = self.arrowCollections[collectionIndex][1]
                # Move boxes
                arrowCollection.remove()
                arrowCollection = Utilities.get_arrows_on_edges(edge_pos=box_pos)
                arrowCollection.set_zorder(2)  # edges go behind nodes
                # boxCollection.set_label(label)
                self.axes.add_collection(arrowCollection)
                self.arrowCollections[collectionIndex] = (self.arrowCollections[collectionIndex][0], arrowCollection)

                collectionIndex += 1

        if color:
            # Update colors
            edgeSize = lambda v, w: self.edgeWidthSize if (v, w) != self.focusEdge else self.edgeWidthSize + 1
            boxSize = lambda v, w: 1 if (v, w) != self.focusEdge else 2
            collectionIndex = 0
            for edges, edgeCollection in self.edgeCollections:
                if edges:
                    edgeColorList = [colorConverter.to_rgba(self.edgeColor(v, w), 1) for v, w in
                                     edges]

                    edgeCollection.set_color(edgeColorList)
                    edgeCollection.set_linewidth([edgeSize(v, w) for v, w in edges])

                    boxCollection = self.boxCollections[collectionIndex][1]
                    boxCollection.set_edgecolor(edgeColorList)
                    boxCollection.set_linewidth([boxSize(v, w) for v, w in edges])

                    arrowCollection = self.arrowCollections[collectionIndex][1]
                    arrowCollection.set_edgecolor(edgeColorList)
                collectionIndex += 1

        # Update edge label texts and positions
        lbls = self.get_edge_labels()
        for edge, label in self.edgeLabelCollection.items():  # type(label) = matplotlib.text.Text object
            v, w = edge
            if self.focusNode is not None:
                if v not in self.focusNode and w not in self.focusNode:
                    # No need to update anything
                    continue

            lblTuple = lbls[(v, w)]
            if label.get_text() != lblTuple:
                label.set_text(lblTuple)
            posv = (self.network.nodes[v]['position'][0] * 0.5, self.network.nodes[v]['position'][1] * 0.5)
            posw = (self.network.nodes[w]['position'][0] * 0.5, self.network.nodes[w]['position'][1] * 0.5)
            pos = (posv[0] + posw[0], posv[1] + posw[1])
            label.set_position(pos)

            rotAngle = Utilities.get_edge_label_rotation(self.axes, posv, posw, pos)
            label.set_rotation(rotAngle)

        self.draw_idle()

    def zoom(self, factor=None):
        """Zoom by factor"""
        if factor is not None:
            smaller = lambda val: factor * val  # Returns smaller value if factor < 1, i.e. if zooming out
            bigger = lambda val: (1. / factor) * val  # Returns bigger value if factor < 1, i.e. if zooming out
        else:
            smaller = lambda val: val
            bigger = lambda val: val

        # Scale axis
        self.Xlim = tuple(bigger(entry) for entry in self.Xlim)
        self.Ylim = tuple(bigger(entry) for entry in self.Ylim)
        self.axes.set_xlim(self.Xlim)
        self.axes.set_ylim(self.Ylim)

        # Scale edge widths
        self.edgeWidthSize = smaller(self.edgeWidthSize)
        # edgeWithSize = max(1, int(round(self.edgeWidthSize)))
        for edges, edgeCollection in self.edgeCollections:
            edgeCollection.set_linewidth(self.edgeWidthSize)

        # Scale font size of node labels
        self.nodeLabelFontSize = smaller(self.nodeLabelFontSize)
        nodeLabelSize = int(round(self.nodeLabelFontSize))
        for v, label in self.nodeLabelCollection.items():
            label.set_fontsize(nodeLabelSize)

        # Scale font size of Additional Node Labels, if existing
        for v, label in self.additionalNodeLabelCollection.items():
            label.set_fontsize(nodeLabelSize)

        # Scale font size of edge labels
        self.edgeLabelFontSize = smaller(self.edgeLabelFontSize)
        edgeLabelSize = int(round(self.edgeLabelFontSize))
        for edge, label in self.edgeLabelCollection.items():
            label.set_fontsize(edgeLabelSize)

        self.draw_idle()

    def move(self):
        """Move field of view"""
        dx = self.mouseWheelPosition[0] - self.mouseWheelPressedPosition[0]
        dy = self.mouseWheelPosition[1] - self.mouseWheelPressedPosition[1]

        self.Xlim = tuple(entry - dx for entry in self.Xlim)
        self.Ylim = tuple(entry - dy for entry in self.Ylim)

        self.axes.set_xlim(self.Xlim)
        self.axes.set_ylim(self.Ylim)

    @staticmethod
    def draw_nodes(G,
                   pos,
                   nodelist=None,
                   node_size=300,
                   node_color='r',
                   node_shape='o',
                   alpha=1.0,
                   cmap=None,
                   vmin=None,
                   vmax=None,
                   ax=None,
                   linewidths=None,
                   label=None,
                   **kwds):
        """Workaround to specify node drawing function"""
        return Utilities.draw_nodes(G,
                                    pos,
                                    nodelist,
                                    node_size,
                                    node_color,
                                    node_shape,
                                    alpha,
                                    cmap,
                                    vmin,
                                    vmax,
                                    ax,
                                    linewidths,
                                    label)

    def draw_edges(self, G, pos,
                   edgelist=None,
                   width=1.0,
                   edge_color='k',
                   style='solid',
                   alpha=1.0,
                   edge_cmap=None,
                   edge_vmin=None,
                   edge_vmax=None,
                   ax=None,
                   arrows=True,
                   label=None,
                   **kwds):
        """Workaround to specify edge drawing function"""

        arrows = self.showArrows
        return Utilities.draw_edges_with_boxes(G, pos,
                                               edgelist,
                                               width,
                                               edge_color,
                                               style,
                                               alpha,
                                               edge_cmap,
                                               edge_vmin,
                                               edge_vmax,
                                               ax,
                                               arrows,
                                               label)
