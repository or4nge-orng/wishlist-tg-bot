import Foundation

@Observable
final class SessionManager {
    static let shared = SessionManager()

    private let userIdKey = "currentUserId"
    private let usernameKey = "currentUsername"
    private let coupleIdKey = "currentCoupleId"
    private let baseURLKey = "apiBaseURL"

    var currentUserId: Int? {
        didSet { persist() }
    }

    var currentUsername: String? {
        didSet { persist() }
    }

    var currentCoupleId: Int? {
        didSet { persist() }
    }

    var baseURL: String {
        didSet { UserDefaults.standard.set(baseURL, forKey: baseURLKey) }
    }

    var isLoggedIn: Bool {
        currentUserId != nil
    }

    var hasCouple: Bool {
        currentCoupleId != nil
    }

    private init() {
        let defaults = UserDefaults.standard
        let storedId = defaults.integer(forKey: userIdKey)
        currentUserId = storedId == 0 ? nil : storedId
        currentUsername = defaults.string(forKey: usernameKey)
        let storedCoupleId = defaults.integer(forKey: coupleIdKey)
        currentCoupleId = storedCoupleId == 0 ? nil : storedCoupleId
        baseURL = defaults.string(forKey: baseURLKey) ?? "https://wishlist-app-or4nge.amvera.io/"
    }

    func login(user: UserDetail) {
        currentUserId = user.id
        currentUsername = user.username
        currentCoupleId = user.coupleId
    }

    func updateCoupleId(_ coupleId: Int?) {
        currentCoupleId = coupleId
    }

    func logout() {
        currentUserId = nil
        currentUsername = nil
        currentCoupleId = nil
    }

    private func persist() {
        let defaults = UserDefaults.standard
        if let currentUserId {
            defaults.set(currentUserId, forKey: userIdKey)
        } else {
            defaults.removeObject(forKey: userIdKey)
        }
        if let currentUsername {
            defaults.set(currentUsername, forKey: usernameKey)
        } else {
            defaults.removeObject(forKey: usernameKey)
        }
        if let currentCoupleId {
            defaults.set(currentCoupleId, forKey: coupleIdKey)
        } else {
            defaults.removeObject(forKey: coupleIdKey)
        }
    }
}
