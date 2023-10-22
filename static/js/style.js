
//-----------------------------------------------------
//  SHOW MORE BUTTON - START
//-----------------------------------------------------
function show_more_list(e){
    let more_list = e.getAttribute("modal")
    let modal = document.getElementById(more_list)
    if(modal.style.display === "block"){
        modal.style.display = "none"
    }else{
        modal.style.display = "block"
    }
}
//-----------------------------------------------------
//  SHOW MORE BUTTON - END
//-----------------------------------------------------
//-----------------------------------------------------
//  MODAL DISPLAY - START
//-----------------------------------------------------
function modal(modal_name,query) {
    var modal = document.getElementById(modal_name);
    if(query == 'show'){
        modal.style.display = 'block'
    }
    if (query == 'hide') {
        modal.style.display = 'none'
    }
}
//-----------------------------------------------------
//  SHOW DISPLAY - END
//-----------------------------------------------------s