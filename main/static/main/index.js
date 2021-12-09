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
    console.log(cause_id)
    fetch(`/causes/v/${cause_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            cause_id: cause_id
        })
    })
    .then(response => response.json())
        .then(result => {
            if ("success" in result) {          
                if (document.querySelector('#vote').innerHTML.trim() == "Vote") {
                    document.querySelector('#vote').innerHTML = "Unvote"
                    ++document.querySelector('#vote-count').innerHTML
                }

                else if (document.querySelector('#vote').innerHTML.trim() == "Unvote") {
                    document.querySelector('#vote').innerHTML = "Vote"
                    if (document.querySelector('#vote-count').innerHTML.trim() != 0) {
                        --document.querySelector('#vote-count').innerHTML
                    }
                }
            }

            else if ("error" in result) {
                document.querySelector('#js-error').innerHTML = result['error']

            }
        })
            .catch(error => {
                console.log(error);
            });

    return false;
    
}

