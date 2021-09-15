
description = 'This is reqres_in API test'

tags = ['Armine']

pages = ['get',
         'post']


def setup(data):
    store('get_users', data.env.url+'api/users')
    store('param', "{'page':2}")


def test(data):
    get.get_url(data.get_users, data.param)
    assert data.last_response.status_code == 200

    post.http_post_upload(data.get_users,idata={"name": "morpheus","job": "leader"})
    response = data.last_response
    assert data.last_response.status_code == 201
    step(str(response.json()))
    step("aaaaaaaaaaaaa")
    for k, v in response.json().items():
        step(k+ ": "+ v)

def teardown(data):
    pass
