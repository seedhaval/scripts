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

/**
 * Class to access Mongo DB from Web UI
 */
class MongoAccess{
    /**
     * Constructor method for MongoAccess class
     */
    constructor(){
        this.app = new App();
        this.div_title = this.app.add_div();
        this.div_form = this.app.add_div();
        this.load_title_div();
    }

    /**
     * Load title div section
     */
    load_title_div(){
        this.div_title.add_title("Access MongoDB");
        this.div_title.add_newline();

        const actions = ["Insert row","Find row","Update row","Delete row"];
        this.dd_action = this.div_title.add_dropdown("Select action",actions,false);
        this.div_title.add_button("Go",this.refresh_form.bind(this),true);
    }

    /**
     * Refresh form based on action selected by user
     */
    refresh_form(opt=undefined){
        this.div_form.clear();
        var typ = this.dd_action.get();
        if( typ == "Insert row" ){
            this.show_insert_form();
        }else if( typ == "Find row" ){
            this.show_read_form();
        }else if( typ == "Update row" ){
            this.show_update_form();
        }else if( typ == "Delete row" ){
            this.show_delete_form();
        }
    }

    /**
     * Show insert form items in form div
     */
    show_insert_form(){
        this.txt_empid = this.div_form.add_text_entry("Employee ID",true);
        this.txt_frst_nm = this.div_form.add_text_entry("First Name",true);
        this.txt_lst_nm = this.div_form.add_text_entry("Last Name",true);
        this.txt_phone = this.div_form.add_text_entry("Phone",true);
        this.div_form.add_button("Insert",this.process_insert_form.bind(this));
    }

    /**
     * Show read form items in form div
     */
    show_read_form(){
        this.txt_empid = this.div_form.add_text_entry("Employee ID",false);
        this.div_form.add_button("Fetch details", this.get_emp_details.bind(this),true);
        this.txt_frst_nm = this.div_form.add_text_entry("First Name",true);
        this.txt_lst_nm = this.div_form.add_text_entry("Last Name",true);
        this.txt_phone = this.div_form.add_text_entry("Phone",true);
    }

    /**
     * Show update form items in form div
     */
    show_update_form(){
        this.txt_empid = this.div_form.add_text_entry("Employee ID",false);
        this.div_form.add_button("Fetch details", this.get_emp_details.bind(this),true);
        this.txt_frst_nm = this.div_form.add_text_entry("First Name",true);
        this.txt_lst_nm = this.div_form.add_text_entry("Last Name",true);
        this.txt_phone = this.div_form.add_text_entry("Phone",true);
        this.div_form.add_button("Update",this.process_update_form.bind(this));
    }

    /**
     * Show delete form items in form div
     */
    show_delete_form(){
        this.txt_empid = this.div_form.add_text_entry("Employee ID",true);
        this.div_form.add_button("Delete", this.process_delete_form.bind(this),true);
    }

    /**
     * Process insert action
     */
    process_insert_form(){
        var data = {"document":{"empid": this.txt_empid.get(), 
        "name": {"first": this.txt_frst_nm.get(), "last": this.txt_lst_nm.get()}
        ,"phone": this.txt_phone.get()}};
        callapi('../insert_data',"POST",data,this.refresh_form.bind(this));
    }

    /**
     * Load employee details based on API response
     * @param {*} rsp 
     */
    load_emp_details( rsp ){
        this.txt_frst_nm.set( rsp["name"]["first"]);
        this.txt_lst_nm.set( rsp["name"]["last"]);
        this.txt_phone.set( rsp["phone"] )
    }

    /**
     * process update action
     */
    process_update_form(){

    }

    /**
     * Process delete action
     */
    process_delete_form(){
        var data = {"empid": this.txt_empid.get()};
        callapi('../delete_data',"POST",data,this.refresh_form.bind(this));
    }

    /**
     * Run AJAX method to get employee details for selected employee ID
     */
    get_emp_details(){
        var data = {"empid": this.txt_empid.get()};
        callapi('../read_data',"POST",data,this.load_emp_details.bind(this));
    }
}