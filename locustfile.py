from locust import FastHttpUser, task, between

class UserBehavior(FastHttpUser):
    wait_time = between(1, 3)  # Waktu tunggu acak antara permintaan (1-3 detik)

    @task(3)
    def get_users(self):
        response = self.client.get("/users")
        print(f"GET /users - Status: {response.status_code} - Response: {response.text}")

    @task(2)
    def get_user(self):
        user_id = 1  # ID pengguna yang akan diuji; sesuaikan sesuai kebutuhan
        response = self.client.get(f"/users/{user_id}")
        print(f"GET /users/{user_id} - Status: {response.status_code} - Response: {response.text}")

    @task(1)
    def create_user(self):
        new_user = {"id": 3, "name": "Cantika", "email": "cantika@example.com"}
        response = self.client.post("/users", json=new_user)
        print(f"POST /users - Status: {response.status_code} - Sent: {new_user} - Response: {response.text}")

    @task(1)
    def update_user(self):
        user_id = 1  # ID pengguna yang akan diperbarui; sesuaikan sesuai kebutuhan
        updated_user = {"id": user_id, "name": "Icca Updated", "email": "icca_updated@example.com"}
        response = self.client.put(f"/users/{user_id}", json=updated_user)
        print(f"PUT /users/{user_id} - Status: {response.status_code} - Sent: {updated_user} - Response: {response.text}")

    @task(1)
    def delete_user(self):
        user_id = 2  # ID pengguna yang akan dihapus; sesuaikan sesuai kebutuhan
        response = self.client.delete(f"/users/{user_id}")
        print(f"DELETE /users/{user_id} - Status: {response.status_code} - Response: {response.text}")

# Perintah untuk menjalankan Locust:
# locust -f locustfile.py --host http://127.0.0.1:8000
