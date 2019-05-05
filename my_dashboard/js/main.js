// Initialize page on load, data is preloaded from the data.js file
window.onload = function(){

  // Initializes the Job Posting sidebar from the data retrieved from our data.js file
  var container = document.getElementsByClassName("w3-bar-block")[0]
  var values = Object.values(postings)
  for(let i = 0; i<values.length; i++){
    var element = document.createElement('a')
    container.appendChild(element)
    element.className = 'w3-bar-item w3-button w3-border-top w3-hover-border-blue'
    element.innerHTML = '<b><i>'+values[i].title+'</i></b>' + ' - ' + values[i].company
    element.setAttribute("href", values[i].link)
    element.setAttribute("target", "_blank")
  }

  // Initializes the weekly deals from the data retrieved from our data.js file
  var container = document.getElementsByClassName('w3-table w3-striped w3-red')[0]
  var keys = Object.keys(deals)
  var values = Object.values(deals)
  for(let i = 0; i<keys.length; i++){
    var tr = document.createElement('tr')
    var td = document.createElement('td')
    var sp = document.createElement('span')
    sp.innerHTML = "<b>"+keys[i]+"</b>" + " - " + "<i>"+values[i]+"</i>"
    container.appendChild(tr).appendChild(td).appendChild(sp)
  }

  // Initializes our watchlist of our stock picks data retrieved from our data.js file
  var container = document.getElementsByClassName('w3-table w3-striped w3-blue')[0]
  var t = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']
  for(let i = 0; i<t.length; i++){
    var tr = document.createElement('tr')
    var td = document.createElement('td')
    var h = document.createElement('h4')
    var sp = document.createElement('span')
    var sp1 = document.createElement('span')
    var sp2 = document.createElement('span')
    var sp3 = document.createElement('span')
    h.innerHTML = t[i]
    sp.innerHTML = "Price: <b>"+stocks[t[i]].price + " (" + "<i>"+stocks[t[i]].change+"</i>" + " %)</b><br>"
    sp1.innerHTML = "MA7: <b>"+stocks[t[i]].maw + "</b>" + "<br>"
    sp2.innerHTML = "MA30: <b>"+stocks[t[i]].mam + "</b>" + "<br>"
    sp3.innerHTML = "MA252: <b>"+stocks[t[i]].maa + "</b>" + "<br><hr>"
    container.appendChild(h)
    container.appendChild(tr).appendChild(td).appendChild(sp)
    container.appendChild(tr).appendChild(td).appendChild(sp1)
    container.appendChild(tr).appendChild(td).appendChild(sp2)
    container.appendChild(tr).appendChild(td).appendChild(sp3)
  }

  // Sets the initial indicator when the webpage first loads from the data retrieved from our data.js file
  var container = document.getElementsByClassName("indicator")
  container[0].innerHTML = '^GSPTSE'
  container[1].innerHTML = "Price: " + "<b>" + stocks['^GSPTSE'].price + " ("+stocks['^GSPTSE'].change+"%)</b>"
  container[2].innerHTML = "MA7: <b>" + stocks['^GSPTSE'].maw + "</b>"
  container[3].innerHTML = "MA30: <b>" + stocks['^GSPTSE'].mam + "</b>"
  container[4].innerHTML = "MA252: <b>" + stocks['^GSPTSE'].maa + "</b>"
}

// Adds functionality to our indicator bars, where a change is made to the data being displayed upon hover
function openIndicator(indi) {
  if(indi == '^GSPTSE' || indi == '^GSPC'){
    var container = document.getElementsByClassName("indicator")
    container[0].innerHTML = indi
    container[1].innerHTML = "Price: " + "<b>" + stocks[indi].price + " ("+stocks[indi].change+"%)</b>"
    container[2].innerHTML = "MA7: <b>" + stocks[indi].maw + "</b>"
    container[3].innerHTML = "MA30: <b>" + stocks[indi].mam + "</b>"
    container[4].innerHTML = "MA252: <b>" + stocks[indi].maa + "</b>"

  } else if(indi == 'BTCUSD' || indi == 'ETHUSD'){
      var container = document.getElementsByClassName("indicator")
      container[0].innerHTML = indi
      container[1].innerHTML = "Price: " + "<b>" + cr[indi].price + " ("+cr[indi].change+"%)</b>"
      container[2].innerHTML = "MA7: <b>" + cr[indi].maw + "</b>"
      container[3].innerHTML = "MA30: <b>" + cr[indi].mam + "</b>"
      container[4].innerHTML = "MA365: <b>" + cr[indi].maa + "</b>"
  } else if(indi == 'USDCAD'){
      var container = document.getElementsByClassName("indicator")
      container[0].innerHTML = indi
      container[1].innerHTML = "Price: " + "<b>" + currency[indi].price + " " + currency[indi].change + "</b>"
      container[2].innerHTML = ""
      container[3].innerHTML = ""
      container[4].innerHTML = ""
  } else if(indi == 'Crude'){
      var container = document.getElementsByClassName("indicator")
      container[0].innerHTML = indi
      container[1].innerHTML = "Price: " + "<b>" + commodity[indi].price + " " + commodity[indi].change + "</b>"
      container[2].innerHTML = ""
      container[3].innerHTML = ""
      container[4].innerHTML = ""
  }
}

// Added functionality of the side menu bar. Template from W3School CSS
// Get the Sidebar:
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverl"<br>" + ay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
    overlayBg.style.display = "none";
  } else {
    mySidebar.style.display = 'block';
    overlayBg.style.display = "block";
  }
}

// Close the sidebar with the close button
function w3_close() {
  mySidebar.style.display = "none";
  overlayBg.style.display = "none";
}
