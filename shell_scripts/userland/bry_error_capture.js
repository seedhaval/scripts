//remap console to some other output
var console = (function(oldCons){
    return {
        log: function(text){
            oldCons.log(text);
						alert( text );
        },
        info: function (text) {
            oldCons.info(text);
						alert( text );
        },
        warn: function (text) {
            oldCons.warn(text);
						alert( text );
        },
        error: function (text) {
            oldCons.error(text);
						alert( text );
        }
    };
}(window.console));

//Then redefine the old console
window.console = console;
