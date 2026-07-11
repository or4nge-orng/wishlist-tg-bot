import Foundation

@Observable
@MainActor
final class WishlistViewModel {
    var wishes: [Wish] = []
    var couple: CoupleDetail?
    var isLoading = false
    var errorMessage: String?

    private let api = APIService.shared
    private let session = SessionManager.shared

    var totalPrice: Double {
        wishes.reduce(0) { $0 + $1.price }
    }

    var formattedTotal: String {
        let formatter = NumberFormatter()
        formatter.numberStyle = .currency
        formatter.currencyCode = "RUB"
        formatter.maximumFractionDigits = 0
        return formatter.string(from: NSNumber(value: totalPrice)) ?? "\(Int(totalPrice)) ₽"
    }

    func loadWishlist() async {
        guard let coupleId = session.currentCoupleId else {
            wishes = []
            couple = nil
            return
        }
        isLoading = true
        errorMessage = nil
        defer { isLoading = false }

        do {
            let detail = try await api.getCouple(id: coupleId)
            couple = detail
            wishes = detail.wishes.sorted { $0.id > $1.id }
        } catch let error as APIError {
            errorMessage = error.errorDescription
        } catch {
            errorMessage = error.localizedDescription
        }
    }

    func deleteWish(_ wish: Wish) async {
        do {
            _ = try await api.deleteWish(id: wish.id)
            wishes.removeAll { $0.id == wish.id }
        } catch let error as APIError {
            errorMessage = error.errorDescription
        } catch {
            errorMessage = error.localizedDescription
        }
    }

    func createWish(name: String, price: Double, url: String, article: Int) async -> Bool {
        guard let coupleId = session.currentCoupleId,
              let userId = session.currentUserId else { return false }

        let request = WishCreateRequest(
            name: name,
            price: price,
            coupleId: coupleId,
            article: article,
            url: url,
            userAddedId: userId
        )

        do {
            let wish = try await api.createWish(request)
            wishes.insert(wish, at: 0)
            return true
        } catch let error as APIError {
            errorMessage = error.errorDescription
            return false
        } catch {
            errorMessage = error.localizedDescription
            return false
        }
    }

    func updateWish(_ wish: Wish, name: String, price: Double, url: String, article: Int, image: String) async -> Bool {
        let request = WishUpdateRequest(
            name: name,
            price: price,
            article: article,
            url: url,
            image: image.isEmpty ? nil : image
        )

        do {
            _ = try await api.updateWish(id: wish.id, body: request)
            if let index = wishes.firstIndex(where: { $0.id == wish.id }) {
                let updated = Wish(
                    id: wish.id,
                    name: name,
                    price: price,
                    article: article,
                    url: url,
                    image: image.isEmpty ? wish.image : image,
                    coupleId: wish.coupleId,
                    userAddedId: wish.userAddedId
                )
                wishes[index] = updated
            }
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
