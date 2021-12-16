document.addEventListener('DOMContentLoaded', function() {    
    
    var edit_btns = document.querySelectorAll('.edit-btn');
    for(var i = 0; i < edit_btns.length; i++){
        edit_btns[i].addEventListener('click', (e) => edit_profile(e));
    }   

    document.querySelector('#post-comment').addEventListener('click', () => post_comment()); 

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


// Edit Profile
// Edit Profile
// Edit Profile
function edit_profile(e) {
    const element = e.target.parentElement.parentElement.firstChild
    console.log(element)
}


// Post Comment function
// Post Comment function
// Post Comment function
function post_comment() {
    const cause_id = document.querySelector('#cause-id').innerHTML;
    const comment = document.querySelector('#comment').value.trim();
    fetch(`/causes/c/${cause_id}`, {
        method: 'POST',
        body: JSON.stringify({
            comment: comment
        })
    })
        .then(response => response.json())
            .then(result => {
            if ("success" in result) {
                let parentElement = document.getElementById('comments')
                let theFirstChild = parentElement.firstChild
                let new_comment = document.createElement('div');
                parentElement.insertBefore(new_comment, theFirstChild);
                new_comment.innerHTML = `
                    <span>${result['username']}:</span> <span class="float-right">${comment}</span>
                    <br>
                    <br>`;
            
                console.log("Successful!")

            }
    
            if ("error" in result) {
                document.querySelector('#to-text-error-message').innerHTML = result['error']
    
            }
            console.log(result);
            })

            .catch(error => {
                console.log(error);
            });
        return false;
}

// Vote Function
// Vote Function
// Vote Function
function vote() {
    let cause_id = document.querySelector('#cause-id').innerHTML.trim();
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
                    ++document.querySelector('#vote-count').innerHTML;
                    var elem = document.getElementById('vote-warning')
                    elem.parentNode.removeChild(elem)
                }

                else if (document.querySelector('#vote').innerHTML.trim() == "Unvote") {
                    document.querySelector('#vote').innerHTML = "Vote"
                    if (document.querySelector('#vote-count').innerHTML.trim() != 0) {
                        --document.querySelector('#vote-count').innerHTML;
                        document.querySelector('#warnings').innerHTML += `<div class="card" id="vote-warning">
                            You have not casted your vote for this month. Please cast your vote to clear this message.
                        </div>`;
                    }
                }
            }

            // else if ("error" in result) {
            //     document.querySelector('#js-error').style.display = 'block';
            //     document.querySelector('#js-error').innerHTML = result['error']
            // }
        })
            .catch(error => {
                console.log(error);
            });

    return false;
    
}

