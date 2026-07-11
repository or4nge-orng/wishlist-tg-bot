import Foundation

enum APIError: LocalizedError {
    case invalidURL
    case invalidResponse
    case httpError(statusCode: Int, message: String)
    case decodingError(Error)
    case networkError(Error)

    var errorDescription: String? {
        switch self {
        case .invalidURL:
            return "Invalid server URL"
        case .invalidResponse:
            return "Invalid server response"
        case .httpError(let code, let message):
            return message.isEmpty ? "Server error (\(code))" : message
        case .decodingError:
            return "Failed to parse server response"
        case .networkError(let error):
            return error.localizedDescription
        }
    }
}
