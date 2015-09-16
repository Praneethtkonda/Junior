$(document).ready(function() {
    $('#teamRegisterForm')
    	.bootstrapValidator({
            feedbackIcons: {
                valid: 'fa fa-check',
                invalid: 'fa fa-times',
                validating: 'fa fa-refresh'
            },
            fields: {
                team_name : {
                    validators : {
                        notEmpty: {
                            message: 'Team Name cannot be empty'  
                        },
                        stringLength: {
                            min: 2,
                            max: 32,
                            message: 'Team Name must be more than 2 and less than 32 characters long'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'TeamName can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                team_school : {
                    validators : {
                        notEmpty: {
                            message: 'Team School cannot be empty'  
                        },
                        stringLength: {
                            min: 2,
                            max: 50,
                            message: 'Team School must be more than 2 and less than 50 characters long'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'Team School can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                member_one : {
                    validators : {
                        notEmpty: {
                            message: 'Member One cannot be empty'  
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address'
                        }, 
                    }
                },
                member_two : {
                    validators : {
                        notEmpty: {
                            message: 'Member Two cannot be empty'  
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address'
                        }, 
                    }
                },
                mentor_name : {
                    validators : {
                        notEmpty: {
                            message: 'Mentor Name cannot be empty'  
                        },
                        stringLength: {
                            min: 4,
                            max: 20,
                            message: 'The Mentor Name must be more than 2 and less than 50 characters long'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'The Mentor Name can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                mentor_email : {
                    validators : {
                        notEmpty: {
                            message: 'Mentor Email cannot be empty'  
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address'
                        }, 
                    }
                },
                mentor_contact : {
                    validators : {
                        notEmpty: {
                            message: 'Mentor Contact cannot be empty'  
                        },
                        regexp: {
                            regexp: /^\+?\d[\d -]{8,13}\d$/,
                            message: 'Not a valid contact number'
                        }
                    }
                },
            }
        });
});
