/**
 * states
 * onclick event handler
 */
const states = document.querySelectorAll('.states');

for(let i = 0; i < states.length; i++){
    const state = states[i]; 
    state.onclick = (e) => {
        const state_id = e.target.dataset['id'];
        console.log(state_id);

        fetch('/main/gyms/' + state_id, {
            method: 'Get'
        })
        .then(response => response.json())
        .then(data => console.log(data));
    }
};



