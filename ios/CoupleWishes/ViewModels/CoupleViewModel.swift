import Foundation

@Observable
@MainActor
final class CoupleViewModel {
    var partnerIdText = ""
    var couple: CoupleDetail?
    var isLoading = false
    var errorMessage: String?
    var successMessage: String?

    private let api = APIService.shared
    private let session = SessionManager.shared

    var partnerName: String? {
        guard let couple, let userId = session.currentUserId else { return nil }
        return couple.users.first(where: { $0.id != userId })?.username
    }

    func loadCouple() async {
        guard let coupleId = session.currentCoupleId else {
            couple = nil
            return
        }
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        do {
            couple = try await api.getCouple(id: coupleId)
        } catch let error as APIError {
            errorMessage = error.errorDescription
        } catch {
            errorMessage = error.localizedDescription
        }
    }

    func createSoloCouple() async -> Bool {
        guard let userId = session.currentUserId else { return false }
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        let request = CoupleCreateRequest(user1Id: userId, user2Id: nil)
        do {
            let response = try await api.createCouple(request)
            session.updateCoupleId(response.id)
            await loadCouple()
            successMessage = "Couple created! Share your ID with your partner."
            return true
        } catch let error as APIError {
            errorMessage = error.errorDescription
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }

    func createCoupleWithPartner() async -> Bool {
        guard let userId = session.currentUserId,
              let partnerId = Int(partnerIdText) else {
            errorMessage = "Enter a valid partner user ID"
            return false
        }
        guard partnerId != userId else {
            errorMessage = "You can't pair with yourself"
            return false
        }

        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        let request = CoupleCreateRequest(user1Id: userId, user2Id: partnerId)
        do {
            let response = try await api.createCouple(request)
            session.updateCoupleId(response.id)
            await loadCouple()
            successMessage = "You're now a couple!"
            return true
        } catch let error as APIError {
            errorMessage = error.errorDescription
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }

    func joinExistingCouple() async -> Bool {
        guard let userId = session.currentUserId,
              let partnerId = Int(partnerIdText) else {
            errorMessage = "Enter your partner's user ID"
            return false
        }

        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        do {
            let partner = try await api.getUser(id: partnerId)
            guard let coupleId = partner.coupleId else {
                errorMessage = "Partner is not in a couple yet"
                return false
            }

            let request = CoupleUpdateRequest(user1Id: partnerId, user2Id: userId)
            _ = try await api.updateCouple(id: coupleId, body: request)
            session.updateCoupleId(coupleId)
            await loadCouple()
            successMessage = "Joined your partner's couple!"
            return true
        } catch let error as APIError {
            errorMessage = error.errorDescription
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }

    func leaveCouple() async -> Bool {
        guard let userId = session.currentUserId else { return false }
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        let request = UserUpdateRequest(username: session.currentUsername, coupleId: 0)
        do {
            _ = try await api.updateUser(id: userId, body: request)
            session.updateCoupleId(nil)
            couple = nil
            return true
        } catch let error as APIError {
            errorMessage = error.errorDescription
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }
}
