window.onload = function () {
    /*Ejecuciones para efecto activo en menuBar*/
    var idd = { id: getPageTitle() };
    active(idd);
    const lb = typeof lightbox === "function" ? lightbox() : '';
    /*Fin de ejecuciones para efecto activo en menuBar*/
}

/*Ejecuciones para efecto activo en menuBar*/
function getPageTitle(){
    var t = document.getElementsByTagName('title')[0];
    if ( !!t.childNodes.length ) {
            if(t.firstChild.data == "Centros" || t.firstChild.data == "Alumnos" || t.firstChild.data == "Cursos"){
                return "centros";
            }else if(t.firstChild.data == "Home"){
                return "inicio"
            }else{
                return t.firstChild.data;
            }
    } else if ( t.innerHTML ) {
              return t.innerHTML;
    }
}
function active(idd) {
    var idds = ["inicio", "centros", "ubicacion", "contacto"];
    for (var id in idds) {
        if (idds[id] == idd.id) {
            $("#" + idds[id]).addClass("activated")
            window.menuActive = idd;
        } else
            $("#" + idds[id]).removeClass("activated")
    }
}
/*Fin de ejecuciones para efecto activo en menuBar*/