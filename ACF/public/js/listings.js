document.getElementById("showR").addEventListener("click",function(){
 
  document.getElementById("gettingRequest").style.display="none";

  document.getElementById("showingRequest").style.display="block";
  

  var A = new Array();

  if(localStorage.getItem('NPORequests') != null)
  {
    A = JSON.parse(localStorage.getItem("NPORequests"));
   
    var tableE = document.createElement('table');
    tableE.id = 'myTable';
    document.getElementById('showingRequest').appendChild(tableE);



    var tableR = document.createElement('tr');
    tableR.id = 'headerRow'
    document.getElementById('myTable').appendChild(tableR);

    var tableH1 = document.createElement('th');
    tableH1.id = 'h1';
    tableH1.innerHTML = 'Kinds';
    document.getElementById('headerRow').appendChild(tableH1);

    var tableH2 = document.createElement('th');
    tableH2.id = 'h2';
    tableH2.innerHTML = 'Information For Artist';
    document.getElementById('headerRow').appendChild(tableH2);

    var tableH3 = document.createElement('th');
    tableH3.id = 'h3';
    tableH3.innerHTML = 'Due Date';
    document.getElementById('headerRow').appendChild(tableH3);


    
    var tableH5 = document.createElement('th');
    tableH5.id = 'h5';
    tableH5.innerHTML = 'name';
    document.getElementById('headerRow').appendChild(tableH5);



    for(i=0; i< A.length; i++){
      

    var tableR = document.createElement('tr');
      tableR.id = 'row' + i;
      document.getElementById('myTable').appendChild(tableR);

      var tableD1 = document.createElement('td');
      tableD1.id = 'd1' + i;
      tableD1.innerHTML = A[i].kinds;
      document.getElementById(tableR.id).appendChild(tableD1);

      var tableD2 = document.createElement('td');
      tableD2.id = 'd2' + i;
      tableD2.innerHTML = A[i].informationForOthers;
      document.getElementById(tableR.id).appendChild(tableD2);

      var tableD3 = document.createElement('td');
      tableD3.id = 'd3' + i ;
      tableD3.innerHTML = A[i].duedate;
      document.getElementById(tableR.id).appendChild(tableD3);

      var tableD5 = document.createElement('td');
      tableD5.id = 'd5' + i;
      
      //var a = document.createElement('a');
      const newHTML = '<a href = "/html/NPO.html">' + A[i].name + '</a>'
      tableD5.innerHTML = newHTML; 
 
      //document.getElementById(tableD5.id).appendChild(a);
      document.getElementById(tableR.id).appendChild(tableD5);
    }
   // <a href=c >ACF</a>


  //console.log(NPORequestsArray.length);
  }
});




