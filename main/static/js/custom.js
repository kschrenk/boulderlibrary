/**
 * states
 * onclick event handler
 */
const states = document.querySelectorAll('.states');

for(let i = 0; i < states.length; i++){
    const state = states[i]; 
    state.onclick = (e) => console.log(state);
};



