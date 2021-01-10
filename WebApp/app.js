function deleteTask(id){
    console.log(id)
    const formData = new FormData()
    formData.append('id', id)
    fetch('http://localhost:5000/rmTask', { 
        method: 'DELETE', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'id': id})
    })
    .then( () => {
        child = document.getElementById(id)
        document.querySelector(".task-container").removeChild(child)
    })
}

fetch('http://localhost:5000/tasksList', {
    method: 'GET',
    headers : { 
      'Content-Type': 'application/json'
     }
   })
.then(response => response.json())
.then(data => {
    let div = document.createDocumentFragment()
    data.payload.tasks.forEach(task => {
        let divTask = document.createElement("DIV")
        divTask.className = "task"
        divTask.setAttribute('id', task.id)
        divTask.innerHTML = `
        <h1>${task.name}</h1>
        Tecnico: <b>${task.technician}</b>
        `
        divTask.addEventListener('click', () => {deleteTask(task.id)})
        div.appendChild(divTask)
    })
    document.querySelector(".task-container").appendChild(div)
})



