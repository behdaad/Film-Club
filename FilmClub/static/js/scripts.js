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

/* main JS */
$('.ui.rating').rating('disable');
$('.film.popup').popup({});
$('#notificationsItem').popup({
    on: 'click',
    inline: true,
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

/* like/comment JS */

var liked1 = false;

$('#likeButton1').click(
    function()
    {
        var count1 = parseInt($('#likeCount1').text());
        if (!liked1)
        {
            $('#likeCount1').text(String(count1 + 1));
            liked1 = true;
            $('#likeButton1').html(
                '<i class="thumbs outline down icon"></i>Unlike'
            );
        }
        else
        {
            $('#likeCount1').text(String(count1 - 1));
            liked1 = false;
            $('#likeButton1').html(
                '<i class="thumbs outline up icon"></i>Like'
            );
        }
    }
);

$('#commentButton1').click(
    function()
    {
        var text = $('#commentText1').val(); // comment text
        if (text !== "")
        {
            $('#comments1').prepend(

                '<div class="comment"> \
                <a class="avatar"> \
                  <img src="img/avatar/steve.jpg"> \
                </a> \
                <div class="content"> \
                  <a class="author" href="userProfile.html">Steve Jobs</a> \
                  <div class="metadata"> \
                    <span class="date">Just Now</span> \
                  </div> \
                  <div class="text">'
                + text +
                '</div> \
              </div> \
            </div>');
            $('#commentText1').val("");
            var cmntCnt1 = parseInt($('#commentsCount1').text()) + 1;
            $('#commentsCount1').text(String(cmntCnt1));
        }
        return false;
    }
);

var liked2 = false;
$('#likeButton2').click(
    function()
    {
        var count2 = parseInt($('#likeCount2').text());
        if (!liked2)
        {
            $('#likeCount2').text(String(count2 + 1));
            liked2 = true;
            $('#likeButton2').html(
                '<i class="thumbs outline down icon"></i>Unlike'
            );
        }
        else
        {
            $('#likeCount2').text(String(count2 - 1));
            liked2 = false;
            $('#likeButton2').html(
                '<i class="thumbs outline up icon"></i>Like'
            );
        }
    }
);

$('#commentButton2').click(
    function()
    {
        var text = $('#commentText2').val(); // comment text
        if (text !== "")
        {
            $('#comments2').prepend(

                '<div class="comment"> \
                <a class="avatar"> \
                  <img src="img/avatar/steve.jpg"> \
                </a> \
                <div class="content"> \
                  <a class="author" href="userProfile.html">Steve Jobs</a> \
                  <div class="metadata"> \
                    <span class="date">Just Now</span> \
                  </div> \
                  <div class="text">'
                + text +
                '</div> \
              </div> \
            </div>');
            $('#commentText2').val("");
            var cmntCnt2 = parseInt($('#commentsCount2').text()) + 1;
            $('#commentsCount2').text(String(cmntCnt2));
        }
        return false;
    }
);

var liked3 = false;
$('#likeButton3').click(
    function()
    {
        var count3 = parseInt($('#likeCount3').text());
        if (!liked3)
        {
            $('#likeCount3').text(String(count3 + 1));
            liked3 = true;
            $('#likeButton3').html(
                '<i class="thumbs outline down icon"></i>Unlike'
            );
        }
        else
        {
            $('#likeCount3').text(String(count3 - 1));
            liked3 = false;
            $('#likeButton3').html(
                '<i class="thumbs outline up icon"></i>Like'
            );
        }
    }
);

$('#commentButton3').click(
    function()
    {
        var text = $('#commentText3').val(); // comment text
        if (text !== "")
        {
            $('#comments3').prepend(

                '<div class="comment"> \
                <a class="avatar"> \
                  <img src="img/avatar/steve.jpg"> \
                </a> \
                <div class="content"> \
                  <a class="author" href="userProfile.html">Steve Jobs</a> \
                  <div class="metadata"> \
                    <span class="date">Just Now</span> \
                  </div> \
                  <div class="text">'
                + text +
                '</div> \
              </div> \
            </div>');
            $('#commentText3').val("");
            var cmntCnt3 = parseInt($('#commentsCount3').text()) + 1;
            $('#commentsCount3').text(String(cmntCnt3));
        }
        return false;
    }
);

/* end like/comment JS */

/* rating a movie JS */

$('.ui .rating').rating('setting', 'clearable', true);

var commentWindowLink = document.getElementById('commentWindow');
commentWindowLink.onclick = function()
{
    var rateValue = $('#commentWindow').rating('get rating');
    if (rateValue > 0)
    {
        $('#rating').text(rateValue);
        $('#commentWindowModel').modal('show');
    }
    return false;
}

/* end rating a movie JS */
