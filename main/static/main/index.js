document.addEventListener('DOMContentLoaded', function() {
    var nav_btns = document.querySelectorAll('.nav-btn');
    for(var i = 0; i < nav_btns.length; i++){
        nav_btns[i].addEventListener('click', (e) => hide_pages(e, nav_btns));
    }   
    var home_btns = document.querySelectorAll('.home-btn');
    for(var i = 0; i < home_btns.length; i++){
        home_btns[i].addEventListener('click', () => homepage());
    }   

    homepage();
});


function hide_pages(e, nav_btns) {
    let page = e.target.innerHTML.trim().toLowerCase();
    document.querySelector('#home').style.display = 'none';
    for (var i = 0; i < nav_btns.length; i++) {
        if (nav_btns[i].innerHTML.trim().toLowerCase() == page) {
            document.querySelector(`#${page}`).style.display = 'block';
        }
        
        else {
            document.querySelector(`#${nav_btns[i].innerHTML.trim().toLowerCase()}`).style.display = 'none';
        }
    }
};

function homepage() {
    document.querySelector('#home').style.display = 'block';
    var nav_btns = document.querySelectorAll('.nav-btn');
    for(var i = 0; i < nav_btns.length; i++){
        document.querySelector(`#${nav_btns[i].innerHTML.trim().toLowerCase()}`).style.display = 'none';
    }
    
    return false;
}