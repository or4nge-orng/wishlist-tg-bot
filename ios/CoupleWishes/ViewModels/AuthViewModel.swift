import Foundation

@Observable
@MainActor
final class AuthViewModel {
    var username = ""
    var password = ""
    var userIdText = ""
    var isLoading = false
    var errorMessage: String?
    var isRegisterMode = true

    private let api = APIService.shared
    private let session = SessionManager.shared

    var isFormValid: Bool {
        if isRegisterMode {
            return username.count >= 3 && password.count >= 8
        }
        return !userIdText.isEmpty && Int(userIdText) != nil
    }

    func register() async -> Bool {
        guard isFormValid else { return false }
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        let newId = Int.random(in: 100_000...999_999_999)
        let request = UserCreateRequest(id: newId, username: username, password: password)

        do {
            _ = try await api.createUser(request)
            let user = try await api.getUser(id: newId)
            session.login(user: user)
            return true
        } catch let error as APIError {
            errorMessage = error.errorDescription
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }

    func login() async -> Bool {
        guard let userId = Int(userIdText) else {
            errorMessage = "Enter a valid user ID"
            return false
        }
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        do {
            let user = try await api.getUser(id: userId)
            session.login(user: user)
            return true
        } catch let error as APIError {
            if case .httpError(let code, _) = error, code == 404 {
                errorMessage = "User not found. Register first."
            } else {
                errorMessage = error.errorDescription
            }
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }

    func refreshSession() async {
        guard let userId = session.currentUserId else { return }
        do {
            let user = try await api.getUser(id: userId)
            session.login(user: user)
        } catch {
            // Keep cached session on network failure
        }
    }
}
