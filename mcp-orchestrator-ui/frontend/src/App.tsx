import Sidebar from './components/Sidebar';
import FlowCanvas from './components/FlowCanvas';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <Sidebar />
      <FlowCanvas />
    </div>
  );
}

export default App;