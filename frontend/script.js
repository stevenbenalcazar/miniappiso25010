document.getElementById("analyzeForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const caso = document.getElementById("caso").value;
    const solucion_usuario = document.getElementById("solucion_usuario").value;
  
    const response = await fetch("http://127.0.0.1:5000/api/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ caso, solucion_usuario }),
    });
  
    const data = await response.json();
  
    if (data.error) {
      alert("Error: " + data.error);
      return;
    }
  
    document.getElementById("solucionIA").textContent = data.solucion_ia;
    document.getElementById("solucionUsuario").textContent = data.solucion_usuario;
    document.getElementById("evaluacion").textContent = data.evaluacion;
  
    document.getElementById("resultados").classList.remove("hidden");
  });
  