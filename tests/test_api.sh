#!/bin/bash
BASE="http://127.0.0.1:5000"

echo "--- Testing Root ---"
curl -s $BASE/ | head -n 10
echo -e "\n"

echo "--- Testing API: Users ---"
echo "1. Add User 'Alice'"
curl -s -X POST $BASE/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "name": "Alice", "email": "alice@example.com"}'
echo -e "\n"

echo "2. Add User 'Jash'"
curl -s -X POST $BASE/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 2, "name": "Jash", "email": "jash@example.com"}'
echo -e "\n"

echo "3. List Users"
curl -s $BASE/api/users/
echo -e "\n"

echo "4. Get User 1"
curl -s $BASE/api/users/1
echo -e "\n"

echo "--- Testing API: Books ---"
echo "5. Add Book 'Clean Code'"
curl -s -X POST $BASE/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin","isbn":"9780132350884","pages":464,"release_date":"2008-08-01","price":33.5}'
echo -e "\n"

echo "6. List Books"
curl -s $BASE/api/books/
echo -e "\n"

echo "7. Get Book by ISBN"
curl -s $BASE/api/books/9780132350884
echo -e "\n"

echo "--- Testing Borrow/Return ---"
echo "8. User 1 Borrows Book"
curl -s -X POST $BASE/api/books/9780132350884/borrow \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1}'
echo -e "\n"

echo "9. User 1 Lists Borrowed Books"
curl -s $BASE/api/users/1/borrowed
echo -e "\n"

echo "10. User 1 Returns Book"
curl -s -X POST $BASE/api/books/9780132350884/return \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1}'
echo -e "\n"

echo "--- Testing Delete ---"
echo "11. Delete User 1"
curl -s -X DELETE $BASE/api/users/1
echo -e "\n"

echo "12. Delete Book"
curl -s -X DELETE $BASE/api/books/9780132350884
echo -e "\n"

echo "--- Testing Admin Pages (HTML) ---"
curl -s $BASE/admin/dashboard | head -n 10
echo -e "\n"
curl -s $BASE/admin/books | head -n 10
echo -e "\n"
curl -s $BASE/admin/users | head -n 10
echo -e "\n"

echo "--- Testing User Pages (HTML) ---"
curl -s $BASE/user/dashboard | head -n 10
echo -e "\n"
curl -s $BASE/user/books | head -n 10
echo -e "\n"

echo "--- All tests complete ---"
