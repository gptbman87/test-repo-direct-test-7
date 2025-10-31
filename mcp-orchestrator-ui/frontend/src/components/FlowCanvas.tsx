import { useState, useCallback } from 'react';
import ReactFlow, { MiniMap, Controls, Background, addEdge, applyEdgeChanges, applyNodeChanges } from 'reactflow';
import type { Node, Edge, OnNodesChange, OnEdgesChange, OnConnect } from 'reactflow';
import 'reactflow/dist/style.css';
import './FlowCanvas.css';

const initialNodes: Node[] = [
  {
    id: '1',
    type: 'input',
    data: { label: 'Start Workflow' },
    position: { x: 250, y: 5 },
    className: 'node-input',
  },
  {
    id: '2',
    data: { label: 'Analyze Data' },
    position: { x: 250, y: 125 },
    className: 'node-default',
  },
  {
    id: '3',
    data: { label: 'Generate Report' },
    position: { x: 500, y: 125 },
    className: 'node-default',
  },
  {
    id: '4',
    type: 'output',
    data: { label: 'End Workflow' },
    position: { x: 250, y: 250 },
    className: 'node-output',
  },
];

const initialEdges: Edge[] = [
    { id: 'e1-2', source: '1', target: '2', animated: true, style: { stroke: '#5e5e5e' } },
    { id: 'e2-3', source: '2', target: '3', animated: true, style: { stroke: '#5e5e5e' } },
    { id: 'e2-4', source: '2', target: '4', animated: true, style: { stroke: '#5e5e5e' } },
];

// Define nodeTypes and edgeTypes as global constants outside the component
const nodeTypes = {};
const edgeTypes = {};

const FlowCanvas = () => {
  const [nodes, setNodes] = useState<Node[]>(initialNodes);
  const [edges, setEdges] = useState<Edge[]>(initialEdges);

  const onNodesChange: OnNodesChange = useCallback(
    (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
    [setNodes]
  );
  const onEdgesChange: OnEdgesChange = useCallback(
    (changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
    [setEdges]
  );
  const onConnect: OnConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges]
  );

  return (
    <div className="flow-canvas">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        fitView
      >
        <Controls />
        <MiniMap />
        <Background />
      </ReactFlow>
    </div>
  );
};

export default FlowCanvas;
