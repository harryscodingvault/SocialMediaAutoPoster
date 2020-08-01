import React from 'react';
import { v4 as uuidv4 } from 'uuid';
import 'bootstrap/dist/css/bootstrap.min.css'; 
import TodoInput from './components/todo-input.component/todo-input.component';
import TodoList from './components/todo-list.component/todo-list.component';



class App extends Component 
{
  state = {
    items: [{ id: 1, title: 'wake up'}, {id:2, title: 'make breakfast'}],
    id: uuidv4(),
    item: '',
    editItem: false
  };

  handleChange = (e) =>;
  handleSubmit = (e) =>;
  clearList = (e) =>;
  handleDelete =  (e) =>;
  handleEdit =  (e) =>;

  return (
    <div className="container">
      <div className='row'>
        <div className='col-10 mx-auto col-md-8 mt-5'>
        <h3 className='text-center text-capitalize'>todo input</h3>
      <TodoInput 
      item={this.state.item} 
      handleChange={this.handleChange} 
      handleSubmit={this.handleSubmit}
      editItem={this.editItem}
      />
        <TodoList 
        item={this.state.item} 
        clearList={this.clearList}
        handleDelete={this.handleDelete}
        handleEdit={this.handleEdit}
        />

        </div>
      </div>
     
    </div>
  );
}

export default App;
