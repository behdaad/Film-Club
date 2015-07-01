/**
 * Created by Behdad on 31/5/15.
 */

/* register.html JS */

$('.ui.dropdown').dropdown();

$('#registerForm')
    .form({
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
    })
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

/* main JS */
$('.ui.rating').rating('disable');
$('.film.popup').popup({});
$('#notificationsItem').popup({
    on: 'click',
    //inline: true,
    transition: 'fade down'
});

$('#closeChat').on("click", function(){
    $('#chatSegment').hide();
    chatOpen = false;
    $('#chatHeader').text("");
});

/* end main JS */

/* search JS */

$('#searchIcon').click(
    function()
    {
        $('#searchForm').submit();
    }
);

var content = [
    {
        title: 'Steve Jobs',
        description: 'User'
    },
    {
        title: 'Steve Jobs',
        description: 'Movie'
    },
    {
        title: 'Inside Job',
        description: 'Movie'
    },
    {
        title: 'The Italian Job',
        description: 'Movie'
    },
    {
        title: 'Enter the Matrix',
        description: 'Movie'
    },
    {
        title: 'Matrix Reloaded',
        description: 'Movie'
    },
    {
        title: 'Matrix Revolutions',
        description: 'Movie'
    },
    {
        title: 'Steven Wilson',
        description: 'User'
    }
];

$('.ui.search').search(
    {
        source: content,
        searchFields: [ 'title' ],
        transition: 'fade down'
    }
);


$('.menu .item').tab();



/* end search JS */

/* chat JS */

var hell;
var chatOpen = false;
$('.chat').on("click", function(){
    if (!chatOpen)
    {
        $('#chatSegment').show();
        hell = $(this);
        var name = $(this).children()[2].children[0].textContent;
        $('#chatHeader').append(name);
        chatOpen = true;
        $('#chatSegment').append(
            '<div class="ui message">\
            Hello! You there?\
          </div>'
        );
        $('#chatSegment').append(
            '<div class="ui blue message">\
            Well yes! How are you man?\
          </div>'
        );

        $('#chatSegment').append(
            '<form class="ui reply form commentForm">\
            <div class="field">\
              <div class="ui action input">\
                <input type="text">\
                <button class="ui small blue icon button commentButton" id="commentButton3">\
                  <i class="comment outline icon"></i>\
                </button>\
              </div>\
            </div>\
          </form>'
        );
    }
});

/* end chat JS */

/* movie review JS */

$('.ui .rating').rating('setting', 'clearable', true);

var commentWindowLink = document.getElementById('commentWindow');
commentWindowLink.onclick = function()
{
    var rateValue = $('#commentWindow').rating('get rating');
    if (rateValue > 0)
    {
        $('#rating').text(rateValue);
        $('#rating_hidden_input').attr('value', rateValue);
        $('#reviewModal')
            .modal({
                onApprove: function()
                {
                    $('#review_form').submit();
                },
                onDeny: function()
                {
                    $('.ui .rating').rating('clear rating');
                }
            })
            .modal('show');
    }
    return false;
};

/* end movie review JS */

/* like/unlike JS */

function like(post_id)
{
    var target_url = '/post/' + post_id + '/like/';
    var xhr = new XMLHttpRequest();
    xhr.open('get', target_url);

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState === 4)
        {
            if(xhr.status === 200)
            {
                var like_button_css_path = '#like_button_' + post_id;
                var target_element = $(like_button_css_path);
                var t = "unlike(" + post_id + ")";
                target_element.attr("onclick", t);
                target_element.html('<i class="thumbs outline down icon"></i>Unlike');

                var like_count_css_path = '#like_count_' + post_id;
                var count1 = parseInt($(like_count_css_path).text());
                $(like_count_css_path).text(String(count1 + 1));
            }
        }
    };
    xhr.send(null);
}

function unlike(post_id)
{
    var target_url = '/post/' + post_id + '/unlike/';
    var xhr = new XMLHttpRequest();
    xhr.open('get', target_url);

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState === 4)
        {
            if(xhr.status === 200)
            {
                var target_css_path = '#like_button_' + post_id;
                var target_element = $(target_css_path);

                target_element.html('<i class="thumbs outline up icon"></i>Like');
                var t = "like(" + post_id + ")";
                target_element.attr("onclick", t);

                var like_count_css_path = '#like_count_' + post_id;
                var count1 = parseInt($(like_count_css_path).text());
                $(like_count_css_path).text(String(count1 - 1));
            }
        }
    };
    xhr.send(null);
}

/* like/unlike JS end */

/* follow/unfollow JS */

function follow(user_id)
{
    var target_url = '/user/' + user_id + '/follow/';
    var xhr = new XMLHttpRequest();

    xhr.open('get', target_url);

    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === 4)
        {
            if (xhr.status === 200)
            {
                var target_css_path = '#follow_button_' + user_id;
                var target_element = $(target_css_path);

                target_element.html('<div class="ui tiny labeled icon red button" onclick="unfollow({{ user.id }})"><i class="remove user icon"></i>Unfollow</div>');
                var t = "unfollow(" + user_id + ")";
                target_element.attr("onclick", t);
            }
        }
    };
    xhr.send(null);
}

function unfollow(user_id)
{
    var target_url = '/user/' + user_id + '/unfollow/';
    var xhr = new XMLHttpRequest();

    xhr.open('get', target_url);

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState === 4)
        {
            if(xhr.status === 200)
            {
                var target_css_path = '#follow_button_' + user_id;
                var target_element = $(target_css_path);

                target_element.html('<div class="ui tiny labeled icon button" onclick="follow({{ user.id }})"><i class="add user icon"></i>Follow</div>');
                var t = "follow(" + user_id + ")";
                target_element.attr("onclick", t);
            }
        }
    };
    xhr.send(null);
}

function follow_profile(user_id)
{
    var target_url = '/user/' + user_id + '/follow/';
    var xhr = new XMLHttpRequest();

    xhr.open('get', target_url);

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState === 4)
        {
            if(xhr.status === 200)
            {
                var target_css_path = '#follow_button_profile_' + user_id;
                var target_element = $(target_css_path);

                target_element.html('<div class="ui red labeled icon button" style="width:62%;"><i class="remove user icon"></i>Unfollow</div>');
                var t = "unfollow_profile(" + user_id + ")";
                target_element.attr("onclick", t);
            }
        }
    };
    xhr.send(null);
}

function unfollow_profile(user_id)
{
    var target_url = '/user/' + user_id + '/unfollow/';
    var xhr = new XMLHttpRequest();

    xhr.open('get', target_url);

    xhr.onreadystatechange = function()
    {
        if(xhr.readyState === 4)
        {
            if(xhr.status === 200)
            {
                var target_css_path = '#follow_button_profile_' + user_id;
                var target_element = $(target_css_path);

                target_element.html('<div class="ui labeled icon button" style="width:62%;" ><i class="add user icon"></i>Follow</div>');
                var t = "follow_profile(" + user_id + ")";
                target_element.attr("onclick", t);
            }
        }
    };
    xhr.send(null);
}

/* follow/unfollow JS end */

/* comment JS */

function comment(post_id, user_id, display_name)
{
    var target_url = '/post/' + post_id + '/comment/';
    var comment_text = $("#comment_text_" + post_id).val();
    // console.log(comment_text);
    if (comment_text !== "")
    {
        $.post(target_url,
            {
                comment_text: comment_text
            },
            function(data, status)
            {
                var avatar_url = data;
                var target_user_url = "/user/" + user_id;
                $('#comments_section_' + post_id).prepend(
                    '<div class="comment">' +
                    '<a href="' + target_user_url + '" class="avatar">' +
                    '<img src="' + avatar_url + '">' +
                    '</a>' +
                    '<div class="content">' +
                    '<a class="author" href="/user/' + user_id + '">' + display_name + '</a>' +
                    '<div class="metadata">' +
                    '<span class="date">Just now</span>' +
                    '</div>' +
                    '<div class="text">' +
                    comment_text +
                    '</div>' +
                    '</div>' +
                    '</div>'
                );
                var comments_count_element = $("#comments_count_" + post_id);
                var comments_count = parseInt(comments_count_element.text()) + 1;
                comments_count_element.text(comments_count);
                comment_text = $("#comment_text_" + post_id).val("")
                return false;
            }
        );
    }
}

function comment_input(event, post_id, user_id, display_name)
{
    // alert("khafan func called");
    if (event.keyCode === 13)
    {
        var target_url = '/post/' + post_id + '/comment/';
        var comment_text = $("#comment_text_" + post_id).val();
        //console.log(comment_text);
        if (comment_text !== "")
        {
            $.post(target_url,
                {
                    comment_text: comment_text
                },
                function(data, status)
                {
                    var avatar_url = data;
                    var target_user_url = "/user/" + user_id;
                    $('#comments_section_' + post_id).prepend(
                        '<div class="comment">' +
                        '<a href="' + target_user_url + '" class="avatar">' +
                        '<img src="' + avatar_url + '">' +
                        '</a>' +
                        '<div class="content">' +
                        '<a class="author" href="/user/' + user_id + '">' + display_name + '</a>' +
                        '<div class="metadata">' +
                        '<span class="date">Just now</span>' +
                        '</div>' +
                        '<div class="text">' +
                        comment_text +
                        '</div>' +
                        '</div>' +
                        '</div>'
                    );
                    var comments_count_element = $("#comments_count_" + post_id);
                    var comments_count = parseInt(comments_count_element.text()) + 1;
                    comments_count_element.text(comments_count);
                    comment_text = $("#comment_text_" + post_id).val("");
                    return false;
                }
            );
        }
    }
}

/* comment JS end */