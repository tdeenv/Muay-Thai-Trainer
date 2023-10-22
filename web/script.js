// Onclick of the button 
document.querySelector("button").onclick = function () {   
  console.log("Button clicked");
  // Call python's generate_combo function 
  eel.generate_combo()(function(combo){                       
    // Update the div with the generated combo returned by python 
    document.querySelector(".combo_text").innerHTML = combo; 
  }) 
} 
