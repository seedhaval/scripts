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
        var data = {"empid": this.txt_empid.get(), "new_values":{ 
        "name": {"first": this.txt_frst_nm.get(), "last": this.txt_lst_nm.get()}
        ,"phone": this.txt_phone.get()}};
        callapi('../update_data',"POST",data,this.refresh_form.bind(this));
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