$(document).ready(function() {
    $('#contactForm')
    	.bootstrapValidator({
            feedbackIcons: {
                valid: 'fa fa-check',
                invalid: 'fa fa-times',
                validating: 'fa fa-refresh'
            },
            fields: {
                name : {
                    validators : {
                        notEmpty: {
                            message: 'Name cannot be empty'  
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'Name can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                body: {
                	validators : {
                        notEmpty: {
                            message: 'Body cannot be empty'
                        },
                    }
                },
                subject: {
                	validators : {
                        notEmpty: {
                            message: 'Subject cannot be empty'
                        },
                    }
                },
                email : {
                    validators : {
                        notEmpty: {
                            message: 'Email cannot be empty'  
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address'
                        }, 
                    }
                },
            }
        });
});
