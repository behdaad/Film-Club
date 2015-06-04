/**
 * Created by Behdad on 31/5/15.
 */

/* register.html JS */

$('.ui.dropdown').dropdown();

$('#registerForm')
    .form(/*{
        firstName: {
            identifier : 'firstName',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter your first name.'
                }
            ]
        },
        lastName: {
            identifier : 'lastName',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter your last name.'
                }
            ]
        },
        date: {
            identifier : 'date',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter your birthday.'
                }
            ]
        },
        gender: {
            identifier : 'gender',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please select your gender.'
                }
            ]
        },
        displayName: {
            identifier : 'displayName',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter a display name.'
                }
            ]
        },
        username: {
            identifier : 'username',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter a username.'
                }
            ]
        },
        password1: {
            identifier : 'password1',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter a password.'
                },
                {
                    type   : 'length[6]',
                    prompt : 'Your password must be at least 6 characters.'
                }
            ]
        },
        password2: {
            identifier : 'password2',
            rules: [
                {
                    type   : 'match[password1]',
                    prompt : 'Your passwords don\'t match.'
                }
            ]
        },
        email: {
            identifier : 'email',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter an email.'
                },
                {
                    type   : 'email',
                    prompt : 'Please enter a valid email.'
                }
            ]
        }
    }*/)
;


/* end register.html JS */



/* login.html JS */

$('#forgotPasswordLink').click(
    function()
    {
        // console.log('forgot password link clicked');
        $('#forgotPasswordModal').modal('show');
        return false;
    }
);

$('#loginForm')
    .form({
        username: {
            identifier : 'username',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter a username.'
                }
            ]
        },
        password: {
            identifier : 'password',
            rules: [
                {
                    type   : 'empty',
                    prompt : 'Please enter a password.'
                }
            ]
        }
    })
;

/* end login.html JS */