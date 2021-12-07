document.addEventListener('DOMContentLoaded', function() {
    
    document.querySelector('#vote').addEventListener('click', () => vote());
});


// function hide_pages(e, nav_btns) {
//     let page = e.target.innerHTML.trim().toLowerCase();
//     document.querySelector('#home').style.display = 'none';
//     for (var i = 0; i < nav_btns.length; i++) {
//         if (nav_btns[i].innerHTML.trim().toLowerCase() == page) {
//             document.querySelector(`#${page}`).style.display = 'block';
//         }
        
//         else {
//             document.querySelector(`#${nav_btns[i].innerHTML.trim().toLowerCase()}`).style.display = 'none';
//         }
//     }
// };

// function homepage() {
//     document.querySelector('#home').style.display = 'block';
//     var nav_btns = document.querySelectorAll('.nav-btn');
//     for(var i = 0; i < nav_btns.length; i++){
//         document.querySelector(`#${nav_btns[i].innerHTML.trim().toLowerCase()}`).style.display = 'none';
//     }
    
//     return false;
// }

function vote() {
    let cause_id = document.querySelector('#cause-id').innerHTML.trim();
    fetch(`causes/v/${cause_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            cause_id: cause_id
        })
    })
    
    if (document.querySelector('#vote').innerHTML == "Vote") {
        document.querySelector('#vote').innerHTML = "Unvote"
    }
    else if (document.querySelector('#vote').innerHTML == "Unvote") {
        document.querySelector('#vote').innerHTML = "Vote"
    }
}

