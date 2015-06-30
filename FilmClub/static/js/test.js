    function comment(post_id, user_id, display_name)
    {
        var target_url = '/post/' + post_id + '/comment/';
        var comment_text = $("#comment_text_" + post_id).val();
        console.log(comment_text);
        if (comment_text !== "")
        {
            $.post(target_url,
                {
                    comment_text: comment_text
                },
                function(data, status)
                {
                    // alert('success! data: ' + data);
                }
            );
            var target_user_url = "/user/" + user_id;
            $('#comments_section_' + post_id).prepend(
                '<div class="comment">' +
                '<a href="' + target_user_url + '" class="avatar">' +
                '<img src="' + '{% static "img/avatar" %}' + '/avatar_' + user_id + '.jpg">' +
                '</a>' +
                '<div class="content">' +
                '<a class="author" href="/user/' + user_id + '">' + display_name + '</a>' +
                '<div class="metadata">' +
                '<span class="date">' + $.now() + '</span>' +
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
    }

    function comment_input(event, post_id, user_id, display_name)
    {
        // alert("khafan func called");
        if (event.keyCode === 13)
        {
            var target_url = '/post/' + post_id + '/comment/';
            var comment_text = $("#comment_text_" + post_id).val();
            console.log(comment_text);
            if (comment_text !== "")
            {
                $.post(target_url,
                    {
                        comment_text: comment_text
                    },
                    function(data, status)
                    {
                        // alert('success! data: ' + data);
                    }
                );
                var target_user_url = "/user/" + user_id;
                $('#comments_section_' + post_id).prepend(
                    '<div class="comment">' +
                    '<a href="' + target_user_url + '" class="avatar">' +
                    '<img src="' + '{% static "img/avatar" %}' + '/avatar_' + user_id + '.jpg">' +
                    '</a>' +
                    '<div class="content">' +
                    '<a class="author" href="/user/' + user_id + '">' + display_name + '</a>' +
                    '<div class="metadata">' +
                    '<span class="date">' + $.now() + '</span>' +
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
        }
    }
