import Foundation

final class APIService {
    static let shared = APIService()

    private let session: URLSession
    private let decoder: JSONDecoder
    private let encoder: JSONEncoder

    private init() {
        let config = URLSessionConfiguration.default
        config.timeoutIntervalForRequest = 30
        session = URLSession(configuration: config)
        decoder = JSONDecoder()
        encoder = JSONEncoder()
    }

    private var baseURL: String {
        SessionManager.shared.baseURL.trimmingCharacters(in: CharacterSet(charactersIn: "/"))
    }

    // MARK: - Users

    func getUsers() async throws -> [UserSummary] {
        try await request(path: "/users/")
    }

    func getUser(id: Int) async throws -> UserDetail {
        try await request(path: "/users/\(id)/")
    }

    func createUser(_ body: UserCreateRequest) async throws -> UserCreateResponse {
        try await request(path: "/users/", method: "POST", body: body)
    }

    func updateUser(id: Int, body: UserUpdateRequest) async throws -> StatusResponse {
        try await request(path: "/users/\(id)", method: "PUT", body: body)
    }

    func deleteUser(id: Int) async throws -> StatusResponse {
        try await request(path: "/users/\(id)", method: "DELETE")
    }

    // MARK: - Couples

    func getCouples() async throws -> [CoupleSummary] {
        try await request(path: "/couples/")
    }

    func getCouple(id: Int) async throws -> CoupleDetail {
        try await request(path: "/couples/\(id)")
    }

    func createCouple(_ body: CoupleCreateRequest) async throws -> CoupleCreateResponse {
        try await request(path: "/couples/", method: "POST", body: body)
    }

    func updateCouple(id: Int, body: CoupleUpdateRequest) async throws -> StatusResponse {
        try await request(path: "/couples/\(id)", method: "PUT", body: body)
    }

    func deleteCouple(id: Int) async throws -> StatusResponse {
        try await request(path: "/couples/\(id)", method: "DELETE")
    }

    // MARK: - Wishes

    func getWishes() async throws -> [Wish] {
        try await request(path: "/wishes/")
    }

    func getWish(id: Int) async throws -> Wish {
        try await request(path: "/wishes/\(id)")
    }

    func createWish(_ body: WishCreateRequest) async throws -> Wish {
        try await request(path: "/wishes/", method: "POST", body: body)
    }

    func updateWish(id: Int, body: WishUpdateRequest) async throws -> StatusResponse {
        try await request(path: "/wishes/\(id)", method: "PUT", body: body)
    }

    func deleteWish(id: Int) async throws -> StatusResponse {
        try await request(path: "/wishes/\(id)", method: "DELETE")
    }

    // MARK: - Core

    private func request<T: Decodable>(
        path: String,
        method: String = "GET",
        body: (any Encodable)? = nil
    ) async throws -> T {
        guard let url = URL(string: baseURL + path) else {
            throw APIError.invalidURL
        }

        var request = URLRequest(url: url)
        request.httpMethod = method
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("application/json", forHTTPHeaderField: "Accept")

        if let body {
            request.httpBody = try encoder.encode(body)
        }

        let data: Data
        let response: URLResponse

        do {
            (data, response) = try await session.data(for: request)
        } catch {
            throw APIError.networkError(error)
        }

        guard let httpResponse = response as? HTTPURLResponse else {
            throw APIError.invalidResponse
        }

        guard (200...299).contains(httpResponse.statusCode) else {
            let message = String(data: data, encoding: .utf8) ?? ""
            throw APIError.httpError(statusCode: httpResponse.statusCode, message: message)
        }

        do {
            return try decoder.decode(T.self, from: data)
        } catch {
            throw APIError.decodingError(error)
        }
    }
}
