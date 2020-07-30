import React, { Component } from 'react'
import Item from './component/todo-item.component/todo-item.component'

export default class TodoList extends Component {
    render() {
        return (
           <section>
            <h2>TODO LIST</h2>
            <Item />
           </section>
        )
    }
}
