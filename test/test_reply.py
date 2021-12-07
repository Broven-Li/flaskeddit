from test import helpers

from passlib.hash import bcrypt

from flaskeddit import db
from flaskeddit.models import AppUser, Community, Post, Reply, ReplyVote


class TestReply:
    def test_get_reply(self, test_client):
        """
        Test GET request to the /community/_/post/_/reply route to assert the create
        reply page is displayed.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.get(
            f"/community/{community.name}/post/{post.title}/reply"
        )

        assert response is not None
        assert response.status_code == 200
        assert b"Create Reply" in response.data

    def test_post_reply(self, test_client):
        """
        Test POST request to the /community/_/post/_/reply route to assert the reply is
        successfully created.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.post(
            f"/community/{community.name}/post/{post.title}/reply",
            data={"reply": "mockreply"},
            follow_redirects=True,
        )

        assert response is not None
        assert response.status_code == 200
        assert b"Successfully created reply" in response.data

    def test_get_update_reply(self, test_client):
        """
        Test GET request to the /community/_/post/_/reply/_/edit route to assert the
        update reply page is displayed.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        reply = Reply(reply="mockreply", app_user=app_user, post=post)
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.add(reply)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.get(
            f"/community/{community.name}/post/{post.title}/reply/{reply.id}/edit"
        )

        assert response is not None
        assert response.status_code == 200
        assert b"Update Reply" in response.data

    def test_post_update_reply(self, test_client):
        """
        Test POST request to the /community/_/post/_/reply/_/edit route to assert the
        reply is successfully updated.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        reply = Reply(reply="mockreply", app_user=app_user, post=post)
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.add(reply)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.post(
            f"/community/{community.name}/post/{post.title}/reply/{reply.id}/edit",
            data={"reply": "mockupdatedreply"},
            follow_redirects=True,
        )

        assert response is not None
        assert response.status_code == 200
        assert b"Successfully updated reply" in response.data

    def test_post_delete_reply(self, test_client):
        """
        Test POST request to the /community/_/post/_/reply/_/delete route to assert the
        reply is successfully deleted.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        reply = Reply(reply="mockreply", app_user=app_user, post=post)
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.add(reply)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.post(
            f"/community/{community.name}/post/{post.title}/reply/{reply.id}/delete",
            follow_redirects=True,
        )

        assert response is not None
        assert response.status_code == 200
        assert b"Successfully deleted reply" in response.data

    def test_post_upvote_reply(self, test_client):
        """
        Test POST request to the /community/_/post/_/reply/_/upvote route to assert the
        user successfully upvotes the reply.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        reply = Reply(reply="mockreply", app_user=app_user, post=post)
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.add(reply)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.post(
            f"/community/{community.name}/post/{post.title}/reply/{reply.id}/upvote"
        )

        assert response is not None
        assert response.status_code == 302
        reply_vote = ReplyVote.query.filter_by(
            user_id=app_user.id, reply_id=reply.id
        ).first()
        assert reply_vote is not None
        assert reply_vote.vote == 1

    def test_post_downvote_reply(self, test_client):
        """
        Test POST request to the /community/_/post/_/reply/_/downvote route to assert
        the user successfully downvotes the reply.
        """
        password = "Mockpassword"
        hashed_password = bcrypt.hash(password)
        app_user = AppUser(username="mockusername", password=hashed_password)
        community = Community(
            name="mockcommunity", description="mockdescription", app_user=app_user
        )
        post = Post(
            title="mockposttitle",
            post="mockpost",
            app_user=app_user,
            community=community,
        )
        reply = Reply(reply="mockreply", app_user=app_user, post=post)
        db.session.add(app_user)
        db.session.add(community)
        db.session.add(post)
        db.session.add(reply)
        db.session.commit()
        helpers.login(test_client, app_user.username, password)

        response = test_client.post(
            f"/community/{community.name}/post/{post.title}/reply/{reply.id}/downvote"
        )

        assert response is not None
        assert response.status_code == 302
        reply_vote = ReplyVote.query.filter_by(
            user_id=app_user.id, reply_id=reply.id
        ).first()
        assert reply_vote is not None
        assert reply_vote.vote == -1
