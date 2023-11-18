function calcular() {
    
  var celsius = document.getElementById('c').value;
  var fahrenheit = document.getElementById('f').value;
  var kelvin = document.getElementById('k').value;

  if (celsius !== "") {
      const url1 = 'http://localhost:8000/soap';
      const soapRequest1 = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="converter">
                          <soapenv:Header/>
                          <soapenv:Body>
                              <con:celsius_to_fahrenheit>
                              <!--Optional:-->
                              <con:celsius>${celsius}</con:celsius>
                              </con:celsius_to_fahrenheit>
                          </soapenv:Body>
                          </soapenv:Envelope>
                          `;

      fetch(url1, {
      method: 'POST',
      headers: {
          'Content-Type': 'text/xml',
      },
      body: soapRequest1,
      })
      .then(response => response.text())
      .then(data => {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(data, 'text/xml');
      const resultado = xmlDoc.querySelector('celsius_to_fahrenheitResult').textContent;

      console.log(resultado);
      fahrenheit2 = document.getElementById('f').value = resultado 
      
      
      const url2 = 'http://localhost:8000/soap';
      const soapRequest2 = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="converter">
              <soapenv:Header/>
              <soapenv:Body>
                <con:fahrenheit_to_kelvin>
                    <!--Optional:-->
                    <con:fahrenheit>${fahrenheit2}</con:fahrenheit>
                </con:fahrenheit_to_kelvin>
              </soapenv:Body>
          </soapenv:Envelope>
                          `;

      fetch(url2, {
      method: 'POST',
      headers: {
          'Content-Type': 'text/xml',
      },
      body: soapRequest2,
      })
      .then(response => response.text())
      .then(data => {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(data, 'text/xml');
      const resultado = xmlDoc.querySelector('fahrenheit_to_kelvinResult').textContent;

      console.log(resultado);
      document.getElementById('k').value = resultado    

      })
      .catch(error => {
      console.error('Erro:', error);
      });



      })
      .catch(error => {
      console.error('Erro:', error);
      });


      
  }

  else if(fahrenheit !== ""){
    const url1 = 'http://localhost:8000/soap';
      const soapRequest1 = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="converter">
                      <soapenv:Header/>
                      <soapenv:Body>
                          <con:fahrenheit_to_celsius>
                            <!--Optional:-->
                            <con:fahrenheit>${fahrenheit}</con:fahrenheit>
                          </con:fahrenheit_to_celsius>
                      </soapenv:Body>
                    </soapenv:Envelope>
                          `;

      fetch(url1, {
      method: 'POST',
      headers: {
          'Content-Type': 'text/xml',
      },
      body: soapRequest1,
      })
      .then(response => response.text())
      .then(data => {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(data, 'text/xml');
      const resultado = xmlDoc.querySelector('fahrenheit_to_celsiusResult').textContent;

      console.log(resultado);
      document.getElementById('c').value = resultado 
      
      
      const url2 = 'http://localhost:8000/soap';
      const soapRequest2 = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="converter">
              <soapenv:Header/>
              <soapenv:Body>
                <con:fahrenheit_to_kelvin>
                    <!--Optional:-->
                    <con:fahrenheit>${fahrenheit}</con:fahrenheit>
                </con:fahrenheit_to_kelvin>
              </soapenv:Body>
          </soapenv:Envelope>
                          `;

      fetch(url2, {
      method: 'POST',
      headers: {
          'Content-Type': 'text/xml',
      },
      body: soapRequest2,
      })
      .then(response => response.text())
      .then(data => {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(data, 'text/xml');
      const resultado = xmlDoc.querySelector('fahrenheit_to_kelvinResult').textContent;

      console.log(resultado);
      document.getElementById('k').value = resultado    

      })
      .catch(error => {
      console.error('Erro:', error);
      });



      })
      .catch(error => {
      console.error('Erro:', error);
      });
  }

  else if(kelvin !== ""){
    const url1 = 'http://localhost:8000/soap';
      const soapRequest1 = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="converter">
                      <soapenv:Header/>
                      <soapenv:Body>
                        <con:kelvin_para_celsius>
                            <!--Optional:-->
                            <con:kelvin>${kelvin}</con:kelvin>
                        </con:kelvin_para_celsius>
                      </soapenv:Body>
                  </soapenv:Envelope>
                          `;

      fetch(url1, {
      method: 'POST',
      headers: {
          'Content-Type': 'text/xml',
      },
      body: soapRequest1,
      })
      .then(response => response.text())
      .then(data => {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(data, 'text/xml');
      const resultado = xmlDoc.querySelector('kelvin_para_celsiusResult').textContent;

      console.log(resultado);
      celsius = document.getElementById('c').value = resultado 
      
      
      const url2 = 'http://localhost:8000/soap';
      const soapRequest2 = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="converter">
                  <soapenv:Header/>
                  <soapenv:Body>
                      <con:celsius_to_fahrenheit>
                      <!--Optional:-->
                      <con:celsius>${celsius}</con:celsius>
                      </con:celsius_to_fahrenheit>
                  </soapenv:Body>
                  </soapenv:Envelope>
                          `;

      fetch(url2, {
      method: 'POST',
      headers: {
          'Content-Type': 'text/xml',
      },
      body: soapRequest2,
      })
      .then(response => response.text())
      .then(data => {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(data, 'text/xml');
      const resultado = xmlDoc.querySelector('celsius_to_fahrenheitResult').textContent;

      console.log(resultado);
      document.getElementById('f').value = resultado    

      })
      .catch(error => {
      console.error('Erro:', error);
      });



      })
      .catch(error => {
      console.error('Erro:', error);
      });
  }
  

}


function limitarEntrada(id) {
  // Recuperar o valor do campo atual
  var valorAtual = document.getElementById(id).value;

  // Desativar outros campos se o campo atual estiver preenchido
  if (valorAtual !== "") {
      if (id !== "c") document.getElementById('c').disabled = true;
      if (id !== "f") document.getElementById('f').disabled = true;
      if (id !== "k") document.getElementById('k').disabled = true;
  } else {
      // Ativar outros campos se o campo atual estiver vazio
      document.getElementById('c').disabled = false;
      document.getElementById('f').disabled = false;
      document.getElementById('k').disabled = false;
  }
}

function limparCampos() {
  // Limpar os campos de entrada
  document.getElementById('c').value = "";
  document.getElementById('f').value = "";
  document.getElementById('k').value = "";

  document.getElementById('k').disabled = false;
  document.getElementById('c').disabled = false;
  document.getElementById('f').disabled = false;
}