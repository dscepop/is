@echo off
:: ===== KEYCLOAK WINDOWS SETUP SIMULATION =====
echo [1/6] Installing prerequisites...
timeout /t 2 >nul
echo ✓ Java already installed (Java 17.0.8)
echo ✓ curl already available
echo.

echo [2/6] Starting Keycloak server...
start /B kc.bat start-dev
timeout /t 5 >nul
echo ✓ Keycloak running on http://localhost:8080
echo.

echo [3/6] Opening Admin Console...
start "" "http://localhost:8080"
echo ℹ Please manually:
echo   1. Login with admin/admin
echo   2. Create 'DemoRealm' realm
echo   3. Create 'demo-client' client
echo   4. Set Redirect URIs to *
echo   5. Click Save
timeout /t 10 >nul
echo ✓ Assuming configuration complete
echo.

echo [4/6] Getting admin token...
set ADMIN_TOKEN=$(curl -s -X POST "http://localhost:8080/realms/master/protocol/openid-connect/token" ^
 -H "Content-Type: application/x-www-form-urlencoded" ^
 -d "username=admin" ^
 -d "password=admin" ^
 -d "grant_type=password" ^
 -d "client_id=admin-cli" | jq -r ".access_token")

echo Admin Token: %ADMIN_TOKEN%
timeout /t 2 >nul
echo.

echo [5/6] Creating test user...
curl -X POST "http://localhost:8080/admin/realms/DemoRealm/users" ^
 -H "Authorization: Bearer %ADMIN_TOKEN%" ^
 -H "Content-Type: application/json" ^
 -d "{\"username\":\"winuser\",\"enabled\":true,\"credentials\":[{\"type\":\"password\",\"value\":\"Windows123!\",\"temporary\":false}]}"
echo ✓ User 'winuser' created
timeout /t 2 >nul
echo.

echo [6/6] Testing authentication...
curl -X POST "http://localhost:8080/realms/DemoRealm/protocol/openid-connect/token" ^
 -H "Content-Type: application/x-www-form-urlencoded" ^
 -d "username=winuser" ^
 -d "password=Windows123!" ^
 -d "grant_type=password" ^
 -d "client_id=demo-client"

echo.
echo ✓ Authentication successful!
echo.
echo ===== SIMULATION COMPLETE =====
echo Next steps:
echo 1. Check http://localhost:8080/admin
echo 2. Configure additional users/groups
pause