import Foundation

struct CoupleSummary: Codable, Identifiable {
    let id: Int
    let users: [UserInCouple]
}

struct CoupleDetail: Codable, Identifiable {
    let id: Int
    let users: [UserInCouple]
    let wishes: [Wish]
}

struct CoupleCreateRequest: Codable {
    let user1Id: Int
    let user2Id: Int?

    enum CodingKeys: String, CodingKey {
        case user1Id = "user1_id"
        case user2Id = "user2_id"
    }
}

struct CoupleCreateResponse: Codable {
    let id: Int
}

struct CoupleUpdateRequest: Codable {
    let user1Id: Int
    let user2Id: Int?

    enum CodingKeys: String, CodingKey {
        case user1Id = "user1_id"
        case user2Id = "user2_id"
    }
}
