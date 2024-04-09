$(function() {
    $.validator.setDefaults({
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).closest('.form-group').removeClass('has-error');
        }
    });

    $('#your-form-id').validate({ // Replace 'your-form-id' with the actual ID of your form
        rules: {
            password: "required",
            dob: "required", // Assuming 'dob' is the ID of your birthDate input field
            weight: {
                required: true,
                number: true
            },
            height: {
                required: true,
                number: true
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            password: {
                required: "Please enter a password"
            },
            dob: {
                required: "Please enter a birthdate"
            },
            email: {
                required: 'Please enter an email',
                email: 'Please enter a valid email'
            },
            weight: {
                required: "Please enter your weight",
                number: "Only numbers are allowed"
            },
            height: {
                required: "Please enter your height",
                number: "Only numbers are allowed"
            },
        }
    });

    // Restrict special characters in Full Name field
    $('#Fname').on('input', function() {
        $(this).val($(this).val().replace(/[^a-zA-Z\s]/g, ''));
    });

    // Restrict phone number to 10 digits
    $('#phone').on('input', function() {
        $(this).val($(this).val().replace(/\D/g, '').substring(0, 10));
    });
});