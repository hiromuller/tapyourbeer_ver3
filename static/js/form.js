var space_key = typeof KeyEvent !== "undefined" ? KeyEvent.DOM_VK_SPACE : 32;
var enter_key = typeof KeyEvent !== "undefined" ? KeyEvent.DOM_VK_ENTER : 13;
var up_key =    typeof KeyEvent !== "undefined" ? KeyEvent.DOM_VK_UP    : 38;
var down_key =  typeof KeyEvent !== "undefined" ? KeyEvent.DOM_VK_DOWN  : 40;

function setup_compy_form(){
    var form = $("form");
    var inputs = form.find("input, textarea");
    var spans = form.find("span");
    var checkboxes = spans.filter(".checkbox");
    var radios = spans.filter(".radio");
    var radio_inputs = inputs.filter("[type=radio]");
    var checkbox_inputs = inputs.filter("[type=checkbox]");
    var spinner_arrows = form.find(".spinner-arrow");
    var underlines = form.find(".underline");
    var underline_inputs = underlines.children("input");
    var underline_labels = underlines.children("label");
    var textareas = inputs.filter("textarea");
    var dropdowns = form.find(".dropdown");
   // var dropdown_options = dropdowns.find("p");
    var labels = form.find("label");
    var dropdown_inputs = dropdowns.find("input");
    var selects = dropdowns.find("select");

    labels.mousedown(function(e){
      e.preventDefault();
    })

    selects.change(function(){
      var select = $(this);
      var container = select.siblings("div");
      set_dropdown_value(container, select.val());
    });

    function set_dropdown_value(container, value){
        var input = container.children("input");
        var placeholder = container.children(".placeholder");

        container.addClass("float-label");

        input.val(value);
        placeholder.hide();
    }

    dropdown_inputs
      .filter(".focus-helper")
          .blur(function(){
              $(this).closest(".dropdown").removeClass("open");
          });


    dropdowns
       .click(function(e){
         var dropdown = $(this);
         var select = dropdown.find("select");

         if(select.size() > 0){

         } else {
             dropdown.toggleClass("open");

             if(dropdown.hasClass("open")){
                var label = dropdown.find("label");

                if(label.hasClass("invalid")){
                  label.text(label.data("text"));
                  label.removeClass("invalid");
                }
                dropdown.find(".focus-helper").focus();

             }
         }
       })
       .mousedown(function(e){
          if(!$(e.target).is("select")){
            e.preventDefault();
          }
       })
       .blur(function(){
         var dropdown = $(this);
         dropdown.removeClass("open");
       })
       .find(".dropdown-box p")
            .mousedown(function(e){
                e.preventDefault();
            })
            .click(function(e){
                var option = $(this);
                var dropdown_box = option.closest(".dropdown-box");
                dropdown_box.removeClass("open");
                set_dropdown_value(dropdown_box.parent(), option.text());
           });



    radio_inputs
       .filter("[checked]")
            .each(function(){
                 activate_radio_input($(this));
             });

    // load previous form data from local storage
    //load_form_data();

    /*
    form.submit(function () {

        if (validate_all()) {
            var $this = $(this);
            var formData = $this.serialize();
            alert(formData);
            return false;
        } else {
            $('html,body').animate({
                scrollTop: $(".invalid").offset().top - 10
            }, 'fast');
            return false;
        }
    });
    */

    textareas.each(function(){
      var textarea = $(this);

      textarea.on('input change cut paste drop keyup', function(){
        $(this)
          .height('auto')
          .height(this.scrollHeight);
      });
    });

    checkboxes
        .click(function () {
            var checkbox = $(this);
            toggle_checkbox_value(checkbox);
            checkbox.focus();
        })
        .keydown(function (e) {
            // check if space is defined
            var key = e.which;

            // space is pressed on focus
            if (key === space_key || key === enter_key) {
                e.preventDefault();
                toggle_checkbox_value($(this));
            }
        })
        .siblings("label")
            .click(function () {
                $(this).siblings(".checkbox").focus();
            });

    radios
        .click(function () {
            var radio = $(this);
            activate_radio_input(radio.siblings("input"));
        })
        .keydown(function (e) {
            // check if space is defined
            var key = e.which;

            // space is pressed on focus
            if (key === space_key || key === enter_key) {
                activate_radio_input($(this).siblings("input"));
            }
        })
        .siblings("label")
            .click(function () {
                var radio = $(this).siblings(".radio");
                activate_radio_input(radio.siblings("input"));
                radio.focus();
            })
            .mousedown(function (e) {
                e.preventDefault();
            });


    inputs
        .each(function () {
            check_label_state($(this));
        })
        .focus(function () {
            var input = $(this);
            set_label_state(input, true);
            $(this).parent().addClass("focused");
            set_input_label_as_valid(input.siblings("label"));
        })
        .blur(function () {
            var input = $(this);
            check_label_state(input);
            input.parent().removeClass("focused");
        });



    inputs.filter("[type=number]")
        .each(function(){
          // fool HTML validation, enable numeric keyboard, but not a spinner widget
          $(this).attr("type", "tel");
        })
        .keydown(function (e) {
            var key = e.which;
            var input = $(this);
            if (key === up_key) {
                step_numeric_input(input.siblings(".up"));
                e.preventDefault();
            } else if (key === down_key) {
                step_numeric_input(input.siblings(".down"));
                e.preventDefault();
            }
        });



    inputs.on("input text change paste drop", function () {
        set_input_label_as_valid($(this).siblings("label"));
    });

    var spinner_hold_timeout = 0;

    spinner_arrows
        .click(function () {
            step_numeric_input($(this));
        })
        .mousedown(function (e) {
            e.preventDefault();
            spinner_hold_timeout = setInterval(function () {
                step_numeric_input($(e.target));
            }, 150);
        })
        .bind('mouseup', function () {
            clearTimeout(spinner_hold_timeout);
        });


    if (!Modernizr.touch) {
        inputs.hover(function () {
            $(this).parent().addClass("input-hover");
        }, function () {
            $(this).parent().removeClass("input-hover");
        });
    }


    function int_css(element, property){
      return parseInt(element.css(property));
    }

    function activate_radio_input(input) {
        var radio = input.siblings(".radio");
        var name = input.attr("name");
        var group = radio_inputs.filter("[name=" + name + "]");

        group.each(function () {
            $(this).prop("checked", false);
        });

        input.prop("checked", true);
    }



    function set_input_label_as_valid(label){
      if (label.hasClass("invalid")) {
            // set label as valid and restore text
            label
              .removeClass("invalid")
              .text(label.data("text"));
        }
    }

    function toggle_checkbox_value(checkbox) {
        var input = checkbox.siblings("input");
        input.prop("checked", !input.prop("checked"));
    }

    function clear_all() {

        underlines
          .filter(".float-label")
            .removeClass("float-label");

       underline_inputs.val("");

        dropdowns.find(".placeholder").show();

        var invalid_labels = underline_labels.filter(".invalid");
        underline_labels.removeClass("invalid");


        setTimeout(function(){
          underline_labels.each(function(){
              var label = $(this);
              label.text(label.data("text"));
          });
        }, 250);

        checkbox_inputs
            .filter(":checked")
                .prop("checked", false);

        $('html, body').animate({
            scrollTop: form.offset().top - 10
        }, 'fast');

        if (Modernizr.localstorage) {
            clear_form_data_from_local_storage();
        }
    }

    function hasAttr(element, attr) {
        return typeof element.attr(attr) !== "undefined";
    }

    function set_input_as_invalid(input){
      var label = input.siblings("label");
      if (!label.hasClass("invalid")) {

            // set error text to required if empty, error if set, otherwise invalid
            var error_text;
        if(hasAttr(input, "required") && input.val() === ""){
             error_text = "Required"
        } else {
             error_text = input.data("error") || "Invalid";
        }
            // set label as invalid, save text for later, and set text to error text
            label
                .addClass("invalid")
                .data("text", label.text())
                .text(error_text);
        }
    }

    function validate_input(input){
        var value = input.val();
        if (hasAttr(input, "required") && value === "") {
            set_input_as_invalid(input);
        } else {
          var validation = input.data('validation');
          if (validation && !validate(validation, value)) {
              set_input_as_invalid(input);
          }
        }
    }

    function validate_all() {
       inputs.each(function(){
          validate_input($(this));
       });
       return $(".invalid").size() === 0;
    }

    function step_numeric_input(arrow) {
        // assumed sanitized

        var input = arrow.siblings("input");
        var step = input.attr("step");


        if (arrow.hasClass("down")) {
            step *= -1;
        }

        var value = satitize_numeric_value(input.val());

        if (value === "") {
            value = step;
        } else {
            value = +(value) + +(step);
        }
        input.val(value);
        input.focus();
    }

    function satitize_numeric_value(value) {
        return value.replace(/[^0-9\+\-]/g, "");
    }

    function set_label_state(input, float_label) {
        if (float_label) {
            input.parent().addClass("float-label");
        } else {
            input.parent().removeClass("float-label");
        }
        // the 0.99 forces consistent AA on webkit
        // http://stackoverflow.com/a/11403025/828867
    }

    function check_label_state(input) {
        var not_empty = input.val().length > 0;
        var is_focus = input.is(":focus");
        set_label_state(input, not_empty || is_focus);
    }

    function save_form_data() {
        if (!Modernizr.localstorage) {
            // no support for html storage, bail out
            return false;
        }

        clear_form_data_from_local_storage();

        inputs.each(function () {
            var input = $(this);
            var type = input.attr("type");
            if (type === "password") {
                // skip password
                return true;
            }
            var name = input.attr("name");
            if (typeof name !== 'undefined') {

                var storage_key = "compyform:" + type + ":" + name;
                var value = input.val();
                if (type === "checkbox" || type === "radio") {
                    if (input.is(":checked")) {
                        localStorage.setItem(storage_key, value);
                    }
                } else {
                    if (value !== null && typeof value !== undefined && value.length > 0) {
                        localStorage.setItem(storage_key, value);
                    }
                }
            }
        });
    }

    function load_form_data() {
        if (!Modernizr.localstorage) {
            // no support for html storage, bail out
            return false;
        }

        inputs.each(function () {
            var input = $(this);
            var type = input.attr("type");
            if (type === "password") {
                // skip password
                return true;
            }

            var name = input.attr("name");
            if (typeof name !== 'undefined') {
                var value = localStorage.getItem("compyform:" + type + ":" + name);
                if (value !== null && typeof value !== undefined) {
                    // set the field data here
                    if (type === "checkbox") {

                        input
                          .prop("checked", true)
                          .siblings(".checkbox")
                              .addClass("checked");

                    } else if (type === "radio") {
                        if (value === input.val()) {
                            activate_radio_input(input);
                        }
                    } else {
                        input.val(value);
                    }
                }
            }
        });
    }
    //inputs.filter("[tabindex=1]").focus();
}

$(document).ready(setup_compy_form);
