import './Sidebar.css';

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2>Agents</h2>
      </div>
      <div className="sidebar-content">
        <p>Drag agents to the canvas</p>
        {/* This will be populated with draggable agent nodes later */}
      </div>
    </aside>
  );
};

export default Sidebar;
