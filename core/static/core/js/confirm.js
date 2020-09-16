function confirmEliminar(id){
    Swal.fire({
        title: '¿Se encuentra seguro?',
        text: "¡No podrá revertir este cambio!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/eliminar_subasta/"+id+"/";
        }
      })
}