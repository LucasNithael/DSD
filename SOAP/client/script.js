const soapEnvelope = `
  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="your-namespace-uri">
    <soapenv:Header/>
    <soapenv:Body>
      <web:celsius_to_fahrenheit>
        <celsius>25</celsius>
      </web:celsius_to_fahrenheit>
    </soapenv:Body>
  </soapenv:Envelope>
`;

const soapSettings = {
  method: 'POST',
  headers: {
    'Content-Type': 'text/xml;charset=UTF-8',
    'SOAPAction': 'your-SOAP-action-uri'
  },
  body: soapEnvelope
};

fetch('http://localhost:8000', soapSettings)
  .then(response => response.text())
  .then(data => {
    // Parser XML (Você pode usar outra biblioteca de análise XML, como DOMParser)
    let parser = new DOMParser();
    let xmlDoc = parser.parseFromString(data, 'text/xml');
    
    // Acesse o resultado desejado no XML
    let result = xmlDoc.getElementsByTagName('return')[0].childNodes[0].nodeValue;
    
    console.log('Resultado:', result);
  })
  .catch(error => {
    console.error('Erro na solicitação SOAP:', error);
  });
