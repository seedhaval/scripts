/**
 * Call an API method
 * @param {String} endpoint 
 * @param {String} type 
 * @param {*} data 
 * @param {*} retfunc 
 */
function callapi( endpoint, type, data, retfunc ) {
	var xhttp = new XMLHttpRequest();
	if( retfunc ){
		xhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				retfunc( JSON.parse(this.responseText) );
			}else if( this.readyState == 4 && this.status != 200) {
				alert( 'API Error' );
			}
		};
	}
	xhttp.open( type, endpoint, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	xhttp.send( JSON.stringify(data) );
}

class Button{
    /**
     * Constructor method for Button class
     * @param {Div} prnt 
     * @param {String} label 
     * @param {*} cback 
     */
    constructor(prnt,label,cback){
        this.elm = document.createElement("button");
        this.elm.innerText = label;
        this.elm.addEventListener("click",cback);
        this.parent = prnt;
        this.parent.elm.appendChild(this.elm);
    }
}

class Textentry{
    /**
     * Constructor method for Textentry class
     * @param {Div} prnt 
     * @param {String} label 
     */
    constructor(prnt,label){
        this.inp_elm = document.createElement("input");
        this.inp_elm.id = label;
        this.lbl_elm = document.createElement("label");
        this.lbl_elm.innerText = label;
        this.lbl_elm.htmlFor = label;
        this.parent = prnt;
        this.parent.elm.appendChild(this.lbl_elm);
        this.parent.elm.appendChild(this.inp_elm);
    }

    /**
     * Get value of text box
     * @returns {String}
     */
    get(){
        return this.inp_elm.value;
    }

    /**
     * Set the value of text box
     * @param {String} txt 
     */
    set(txt){
        this.inp_elm.value = txt;
    }
}

class Dropdown{
    /**
     * Constructor method for Dropdown class
     * @param {Div} prnt 
     * @param {String} label 
     * @param {Array} options 
     */
    constructor(prnt,label,options){
        this.sel_elm = document.createElement("select");
        this.sel_elm.id = label;
        this.lbl_elm = document.createElement("label");
        this.lbl_elm.innerText = label;
        this.lbl_elm.htmlFor = label;
        this.options = options;
        this.refresh_options(options);
        this.parent = prnt;
        this.parent.elm.appendChild(this.lbl_elm);
        this.parent.elm.appendChild(this.sel_elm);
    }

    /**
     * Clear the dropdown list
     */
    clear(){
        var len = this.options.length - 1;
        for( var i = len; i >= 0; i-- ){
            this.sel_elm.remove(i);
        }
    }

    /**
     * Change options in the list
     * @param {Array} options 
     */
    refresh_options(options){
        this.clear();
        this.options = options;
        var len = this.options.length;
        for( var i=0; i < len; i++){
            var opt = document.createElement("option");
            opt.value = this.options[i];
            opt.innerHTML = this.options[i];
            this.sel_elm.appendChild(opt);
        }
    }

    /**
     * Get selected value from drop down
     * @returns {String}
     */
    get(){
        return this.sel_elm.value;
    }
}

class Div{
    /**
     * Constructor method for Div class
     * @param {App} prnt 
     */
    constructor(prnt){
        this.elm = document.createElement("div");
        this.parent = prnt;
        this.parent.elm.appendChild(this.elm)
        this.children = [];
    }

    /**
     * Add h1 element to div
     * @param {String} txt 
     * @returns {Node}
     */
    add_title(txt){
        var elm = document.createElement("h1");
        elm.innerText = txt;
        this.children.push(elm);
        this.elm.appendChild(elm)
        return this.elm;
    }

    /**
     * Add a br element to div
     * @returns Node
     */
    add_newline(){
        var elm = document.createElement("br");
        this.children.push(elm);
        this.elm.appendChild(elm)
        return this.elm;
    }

    /**
     * Add dropdown to Div
     * @param {String} label 
     * @param {Array} options 
     * @param {Boolean} append_newline
     * @returns {Dropdown}
     */
    add_dropdown(label,options,append_newline){
        var dd = new Dropdown(this,label,options);
        this.children.push(dd)
        if( append_newline == true){
            this.add_newline();
        }
        return dd;
    }

    /**
     * Add text entry input to Div
     * @param {String} label 
     * @param {Boolean} append_newline
     * @returns {Textentry}
     */
    add_text_entry(label,append_newline){
        var txt = new Textentry(this,label);
        this.children.push(txt);
        if( append_newline == true){
            this.add_newline();
        }
        return txt;
    }

    /**
     * Add button element to Div
     * @param {String} label 
     * @param {*} cback
     * @param {Boolean} append_newline
     * @returns {Textentry}
     */
     add_button(label,cback,append_newline){
        var btn = new Button(this,label,cback);
        this.children.push(btn);
        if( append_newline == true){
            this.add_newline();
        }
        return btn;
    }

    /**
     * Clear contents of div
     */
    clear(){
        this.elm.innerHTML = "";
    }
}

class App{
    /**
     * Constructor method for App class
     */
    constructor(){
        this.elm = document.body;
        this.children = [];
    }

    /**
     * Add div to body
     * @returns {Div}
     */
    add_div() {
        var dv = new Div(this);
        this.children.push(dv)
        return dv;
    }
}
