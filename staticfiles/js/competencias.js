document.addEventListener('DOMContentLoaded', function() {
    const competenciaSelect = document.getElementById('id_fk_id_competencia');
    const maxCompetencias = 3; // Establece el número máximo de competencias que se pueden elegir
  
    if (competenciaSelect) {
      const competenciaOptions = competenciaSelect.options;
      let competenciasSeleccionadas = 0;
  
      competenciaSelect.addEventListener('change', function() {
        competenciasSeleccionadas = [...competenciaOptions].filter(option => option.selected).length;
  
        if (competenciasSeleccionadas >= maxCompetencias) {
          // Deshabilita las competencias no seleccionadas
          [...competenciaOptions].forEach(option => {
            if (!option.selected) {
              option.disabled = true;
            }
          });
        } else {
          // Habilita todas las competencias
          [...competenciaOptions].forEach(option => {
            option.disabled = false;
          });
        }
      });
    }
  });
  