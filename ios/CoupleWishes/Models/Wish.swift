import Foundation

struct Wish: Codable, Identifiable, Hashable {
    let id: Int
    let name: String
    let price: Double
    let article: Int
    let url: String
    let image: String?
    let coupleId: Int
    let userAddedId: Int?

    enum CodingKeys: String, CodingKey {
        case id, name, price, article, url, image
        case coupleId = "couple_id"
        case userAddedId = "user_added_id"
    }

    var formattedPrice: String {
        let formatter = NumberFormatter()
        formatter.numberStyle = .currency
        formatter.currencyCode = "RUB"
        formatter.maximumFractionDigits = 0
        return formatter.string(from: NSNumber(value: price)) ?? "\(Int(price)) ₽"
    }

    var hasURL: Bool {
        !url.isEmpty && URL(string: url) != nil
    }

    var hasImage: Bool {
        guard let image, !image.isEmpty else { return false }
        return URL(string: image) != nil
    }
}

struct WishCreateRequest: Codable {
    let name: String
    let price: Double
    let coupleId: Int
    let article: Int
    let url: String
    let userAddedId: Int

    enum CodingKeys: String, CodingKey {
        case name, price, article, url
        case coupleId = "couple_id"
        case userAddedId = "user_added_id"
    }
}

struct WishUpdateRequest: Codable {
    let name: String
    let price: Double?
    let article: Int?
    let url: String?
    let image: String?
}
