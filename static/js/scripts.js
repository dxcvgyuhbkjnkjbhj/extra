function confirmDelete(taskId) {
    if (confirm('¿Seguro que quieres eliminar esta tarea?')) {
        window.location.href = '/delete/' + taskId;
    }
}
