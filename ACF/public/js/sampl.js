fetch("NPO.json")
  .then(response => 
  {
    console.log(response)
    return response.json()
  })
  .then(response => console.log(response.NPO[0]))
  .catch(error => {console.error()})
