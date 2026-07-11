import Foundation

struct UserSummary: Codable, Identifiable, Hashable {
    let id: Int
    let username: String?
    let coupleId: Int?

    enum CodingKeys: String, CodingKey {
        case id, username
        case coupleId = "couple_id"
    }
}

struct UserDetail: Codable, Identifiable {
    let id: Int
    let username: String?
    let coupleId: Int?
    let message: String?
    let status: Bool?

    enum CodingKeys: String, CodingKey {
        case id, username, message, status
        case coupleId = "couple_id"
    }
}

struct UserInCouple: Codable, Identifiable, Hashable {
    let id: Int
    let username: String
}

struct UserCreateRequest: Codable {
    let id: Int
    let username: String
    let password: String
}

struct UserUpdateRequest: Codable {
    let username: String?
    let coupleId: Int?

    enum CodingKeys: String, CodingKey {
        case username
        case coupleId = "couple_id"
    }
}

struct UserCreateResponse: Codable {
    let id: Int
    let username: String?
    let password: String?
    let coupleId: Int?

    enum CodingKeys: String, CodingKey {
        case id, username, password
        case coupleId = "couple_id"
    }
}

struct StatusResponse: Codable {
    let status: String
    let message: String?
}
