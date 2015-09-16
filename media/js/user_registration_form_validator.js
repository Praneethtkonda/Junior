$(document).ready(function() {
    $('#registerForm')
    	.bootstrapValidator({
            feedbackIcons: {
                valid: 'fa fa-check',
                invalid: 'fa fa-times',
                validating: 'fa fa-refresh'
            },
            fields: {
                firstname : {
                    validators : {
                        notEmpty: {
                            message: 'Firstname cannot be empty'  
                        },
                        stringLength: {
                            min: 4,
                            max: 20,
                            message: 'Firstname must be more than 4 and less than 20 characters long'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'Firstname can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                lastname : {
                    validators : {
                        notEmpty: {
                            message: 'Lastname cannot be empty'  
                        },
                        stringLength: {
                            min: 1,
                            max: 20,
                            message: 'Lastname must be more than 1 and less than 20 characters long'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'Lasttname can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                date_of_birth : {
                    validators: {
                        date: {
                            message: 'The date is not valid',
                            format: 'DD/MM/YYYY'
                        }
                    }
                },
                gender : {
                    validators : {
                        notEmpty: {
                            message: 'Gender cannot be empty'
                        },
                    }
                },
                address: {
                	validators : {
                        notEmpty: {
                            message: 'Address cannot be empty'
                        },
                    }
                },
                state: {
                	validators : {
                        notEmpty: {
                            message: 'State cannot be empty'
                        },
                    }
                },
                city: {
                	validators : {
                        notEmpty: {
                            message: 'City cannot be empty'
                        },
                    }
                },
                pincode : {
                	validators : {
                		notEmpty: {
                			message: 'Pincode cannot be empty'
                		},
                		regexp: {
                			regexp: /^\d{6}$/,
                			message: 'Pincode must be in between 110000 and 799999'
                		}
                	}
                },
                contact_no : {
                    validators : {
                        notEmpty: {
                            message: 'Contact cannot be empty'  
                        },
                        regexp: {
                            regexp: /^\d{10}$/,
                            message: 'Not a valid contact number'
                        }
                    }
                },
                standard: {
                	validators : {
                        notEmpty: {
                            message: 'Standard cannot be empty'
                        },
                    }
                },
                school: {
                	validators : {
                        notEmpty: {
                            message: 'School cannot be empty'
                        },
                    }
                },
                school_address: {
                	validators : {
                        notEmpty: {
                            message: 'School Address cannot be empty'
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
                username : {
                    validators : {
                        notEmpty: {
                            message: 'The username cannot be empty'  
                        },
                        stringLength: {
                            min: 4,
                            max: 20,
                            message: 'The username must be more than 4 and less than 20 characters long'
                        },
                        regexp: {
                            regexp: /^[a-zA-Z0-9_]+$/,
                            message: 'The username can only consist of alphabetical, number and underscore'
                        }
                    }
                }, 
                password: {
                    validators: {
                        notEmpty: {
                            message: 'The password cannot be empty'  
                        },
                        stringLength: {
                            min: 4,
                            max: 32,
                            message: 'The password length must be in b/n 4 and 32 characters long.\nIt should have at least a small and capital letters, digit and special character'
                        },
                        regexp: {
                            regexp: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,32}$/
                        }
                    }
                },
                repass: {
                    validators: {
                        notEmpty: {
                            message: 'The confirm password cannot be empty'  
                        },  
                        regexp: {
                            regexp: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,32}$/
                        },
                        identical: {
                            field: 'password',
                            message: 'The password and the confirm password doesn\'t match'
                        }
                    }
                },
                id_card: {
                	validators : {
                        notEmpty: {
                            message: 'ID Card upload cannot be empty'
                        },
                    }
                },
            }
        });
});