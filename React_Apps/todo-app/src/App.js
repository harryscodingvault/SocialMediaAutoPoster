import React from 'react';
import uuid from 'uuid';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import TodoInput from './components/todo-input.component/todo-input.component';
import TodoList from './components/todo-list.component/todo-list.component';

function App() {
  return (
    <div className="App">
      <TodoInput/>
      <TodoList/>
    </div>
  );
}

export default App;
